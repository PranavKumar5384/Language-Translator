from langcodes import Language
from gtts.lang import tts_langs

def get_full_language_name(code):
    try:
        return Language.get(code).display_name()
    except:
        return code

def list_supported_languages():
    gtts_supported = tts_langs()
    return {code: Language.get(code).display_name() for code in gtts_supported}
