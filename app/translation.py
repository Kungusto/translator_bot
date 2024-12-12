from deep_translator import GoogleTranslator

def translate(word, target_lang='ru'):
    try:
        # Используем Google Translator через deep_translator
        translation = GoogleTranslator(source='auto', target=target_lang).translate(word)
        return translation
    except Exception as e:
        return f"Error: {str(e)}"