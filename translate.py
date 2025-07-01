from googletrans import Translator

translator = Translator()

def detect_language(text):
    detection = translator.detect(text)
    return detection.lang

def translate_text(text, dest_language, src_language=None):
    if src_language:
        translation = translator.translate(text, src=src_language, dest=dest_language)
    else:
        translation = translator.translate(text, dest=dest_language)
    return translation.text
