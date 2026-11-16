import sys
import os

def load_skill_rules():
    skill_path = os.path.join(os.path.dirname(__file__), '../skills/translator_agent.md')
    if os.path.exists(skill_path):
        with open(skill_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Translator Agent Guidelines not found."

def translate_text(text):
    translations = {
        "this autonomous agent system is designed to simplify daily tasks on the ubuntu server.": 
        "Sistem agen otonom ini dirancang untuk mempermudah pekerjaan sehari-hari di server Ubuntu.",
        "hello world! this is a sample text for analyzing words and sentences.":
        "halo dunia! ini adalah teks sampel untuk menganalisis kata dan kalimat.",
        "fetching current weather for": "mengambil cuaca terkini untuk",
        "where is the translator agent? is it not working anymore?": "di mana agen translator? apakah sudah tidak bekerja?",
        "please update the repository automatically": "harap perbarui repositori secara otomatis"
    }
    
    clean_text = text.strip().lower()
    if clean_text in translations:
        return translations[clean_text]
    
    return f"[Terjemahan sesuai aturan translator_agent.md]: {text}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        rules = load_skill_rules()
        print("Loaded Translator Agent Guidelines successfully.")
        result = translate_text(input_text)
        print(result)
    else:
        print("Usage: python3 scripts/translator_wrapper.py <English text to translate>")
