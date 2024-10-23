import json

class LocalizationManager:
    def __init__(self):
        self.translations = {}
        self.current_language = 'en'

    def load_language_file(self, language_code, file_path):
        with open(file_path, 'r') as f:
            self.translations[language_code] = json.load(f)

    def set_language(self, language_code):
        if language_code in self.translations:
            self.current_language = language_code
        else:
            raise ValueError(f"Language {language_code} not found")

    def get_translation(self, key, **kwargs):
        translation = self.translations[self.current_language].get(key, key)
        return translation.format(**kwargs)

if __name__ == "__main__":
    manager = LocalizationManager()

    manager.load_language_file('en', 'data/locales/en.json')
    manager.load_language_file('es', 'data/locales/es.json')
    manager.load_language_file('sv', 'data/locales/sv.json')

    print(manager.get_translation("welcome_message", name="Alice"))
    print(manager.get_translation("items_count", count=5))
    print(manager.get_translation("new_messages", count=1))
    print(manager.get_translation("farewell"))
