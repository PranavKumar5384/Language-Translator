from gtts import gTTS

def text_to_speech(text, lang='en', output_path='tts_output.mp3'):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        return output_path
    except Exception as e:
        print("TTS generation failed:", e)
        return None
