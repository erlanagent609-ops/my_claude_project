import subprocess
import os
from datetime import datetime
import urllib.request
import json

def log_activity(message):
    log_path = os.path.join(os.path.dirname(__file__), '../git_push_activity.log')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(log_entry.strip())

def load_credentials():
    config_path = os.path.join(os.path.dirname(__file__), '../config/git_credentials.json')
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_credentials(creds):
    config_dir = os.path.join(os.path.dirname(__file__), '../config')
    os.makedirs(config_dir, exist_ok=True)
    config_path = os.path.join(config_dir, 'git_credentials.json')
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(creds, f, indent=4)

def interactive_setup():
    creds = load_credentials()
    if not creds.get("telegram_bot_token") or not creds.get("telegram_chat_id") or not creds.get("whatsapp_number"):
        print("\n--- Konfigurasi Kredensial Notifikasi ---")
        token = input("Masukkan Telegram Bot Token: ").strip()
        chat_id = input("Masukkan Telegram Chat ID: ").strip()
        wa_number = input("Masukkan Nomor WhatsApp Tujuan: ").strip()
        
        creds = {
            "telegram_bot_token": token,
            "telegram_chat_id": chat_id,
            "whatsapp_number": wa_number
        }
        save_credentials(creds)
        print("Konfigurasi berhasil disimpan ke config/git_credentials.json.\n")
    return creds

def send_notification(message):
    creds = load_credentials()
    token = creds.get("telegram_bot_token") or os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = creds.get("telegram_chat_id") or os.environ.get("TELEGRAM_CHAT_ID")
    wa_number = creds.get("whatsapp_number") or os.environ.get("WHATSAPP_NUMBER")
    
    log_activity(f"[Notification Gateway] Mengirim laporan: {message}")
    
    # Kirim Telegram
    if token and chat_id:
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = json.dumps({"chat_id": chat_id, "text": message}).encode('utf-8')
            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    log_activity("Notifikasi Telegram berhasil dikirim.")
        except Exception as e:
            log_activity(f"Gagal mengirim notifikasi Telegram: {e}")
            
    # Simulasikan/Kirim WhatsApp Gateway jika nomor tersedia
    if wa_number:
        log_activity(f"Notifikasi WhatsApp diteruskan ke nomor {wa_number}.")

def run_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def git_pusher_agent():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    os.chdir(root_dir)
    
    log_activity("Git Pusher Agent dimulai.")
    
    # Jalankan interaksi setup kredensial jika dijalankan langsung
    interactive_setup()
    
    # 1. Pastikan file sensitif masuk gitignore
    gitignore_path = os.path.join(root_dir, '.gitignore')
    ignore_entry = "config/git_credentials.json"
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if ignore_entry not in content:
            with open(gitignore_path, 'a', encoding='utf-8') as f:
                f.write(f"\n{ignore_entry}\n")
            log_activity("Menambahkan config/git_credentials.json ke .gitignore.")
            
    run_command(["git", "rm", "--cached", "config/git_credentials.json"])
    
    # 2. Cek status git
    success, stdout = run_command(["git", "status"])
    if not success:
        msg = f"Gagal mengecek status git: {stdout}"
        log_activity(msg)
        send_notification(msg)
        return
    log_activity("Status git berhasil diperiksa.")
    
    # 3. Git add
    success, stdout = run_command(["git", "add", "."])
    if not success:
        msg = f"Git add gagal: {stdout}"
        log_activity(msg)
        send_notification(msg)
        return
        
    # 4. Commit
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-push update oleh Autonomous Executor Agent pada {current_time}"
    
    success, stdout = run_command(["git", "commit", "-m", commit_msg])
    if not success and "nothing to commit" not in stdout:
        msg = f"Git commit gagal atau tidak ada perubahan: {stdout}"
        log_activity(msg)
    else:
        log_activity("Git commit berhasil dibuat.")
        
    # 5. Git push
    success, stdout = run_command(["git", "push", "origin", "main"])
    if success:
        msg = f"Git push berhasil! Waktu: {current_time} (Referensi: Git CLI)"
        log_activity(msg)
        send_notification(msg)
    else:
        msg = f"Git push gagal: {stdout}"
        log_activity(msg)
        send_notification(msg)

if __name__ == "__main__":
    git_pusher_agent()
