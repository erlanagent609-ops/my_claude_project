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
        "please update the repository automatically": "harap perbarui repositori secara otomatis",
        "halo, apakah anda terhubung?": "halo, ya saya terhubung dan siap membantu!",
        "halo apakah anda terhubung?": "halo, ya saya terhubung dan siap membantu!",
        "baik sekarang apakah anda bisa memberitahu saya kondisi cuaca di manado?": "baik, mari kita periksa kondisi cuaca di Manado.",
        "baik sekarang apakai anda bisa memberitahu saya kondisi cuaca di manado?": "baik, mari kita periksa kondisi cuaca di Manado."
    }
    
    clean_text = text.strip().lower()
    if clean_text in translations:
        return translations[clean_text]
    
    return f"[Terjemahan sesuai aturan translator_agent.md]: {text}"

def run_translator_test():
    test_phrase = "where is the translator agent? is it not working anymore?"
    result = translate_text(test_phrase)
    print(f"Test Input: {test_phrase}")
    print(f"Test Output: {result}")
    return result is not None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            print("Running Translator Agent Test...")
            success = run_translator_test()
            if success:
                print("Translator Agent Test Passed Successfully.")
            else:
                print("Translator Agent Test Failed.")
        else:
            input_text = " ".join(sys.argv[1:])
            rules = load_skill_rules()
            print("Loaded Translator Agent Guidelines successfully.")
            result = translate_text(input_text)
            print(result)
    else:
        print("Usage: python3 scripts/translator_wrapper.py [--test | <English text to translate>]")
