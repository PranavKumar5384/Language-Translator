import streamlit as st
import os
import tempfile
from video_utils import extract_audio_from_video, save_translated_audio, combine_audio_with_video
from transcribe import transcribe_audio
from translate import translate_text,detect_language
from utils import get_full_language_name, list_supported_languages

st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌍 Language Translator")

st.sidebar.header("Settings")
target_lang = st.sidebar.selectbox("Select Target Language", list(list_supported_languages().values()), index=27)
input_lang_override = st.sidebar.selectbox("Override Input Language (Optional)", ["Auto-detect"] + list(list_supported_languages().values()))

st.markdown("""
This app allows you to:
- Upload an audio or video file
- Translate the audio to a language of your choice
- Create a translated video with the new audio
""")

input_mode = st.radio("Choose Input Mode", ("Upload Audio/Video", "Speech Input", "Text Input"))

input_text = ""

if input_mode == "Upload Audio/Video":
    uploaded_file = st.file_uploader("Upload an audio or video file", type=["mp3", "wav", "mp4", "m4a"])
    
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        
        file_ext = os.path.splitext(uploaded_file.name)[-1][1:]
        if file_ext in ["mp3", "wav", "m4a"]:
            st.audio(uploaded_file, format=f"audio/{file_ext}")
        else:
            st.video(uploaded_file)

        st.subheader("Processing the video...")
        try:
            
            audio_path = extract_audio_from_video(temp_file_path)
            if audio_path:
                st.write("Audio extracted successfully.")

            
            input_text = transcribe_audio(audio_path)
            st.write(f"Original Transcribed Text:\n{input_text}")

           
            if input_lang_override != "Auto-detect":
                source_lang_code = [k for k, v in list_supported_languages().items() if v == input_lang_override][0]
            else:
                source_lang_code = detect_language(input_text)

            target_lang_code = [k for k, v in list_supported_languages().items() if v == target_lang][0]

            translated_text = translate_text(input_text, target_lang_code, source_lang_code)
            st.write(f"Translated Text: {translated_text}")

            translated_audio_path = save_translated_audio(translated_text, target_lang_code)

            if translated_audio_path:
                st.write("Translated audio generated successfully.")
                
                output_video_path = "translated_video.mp4"
                final_video = combine_audio_with_video(temp_file_path, translated_audio_path, output_video_path)

                if final_video:
                    st.video(final_video)
                    st.write(f"Your translated video is ready: {final_video}")
                else:
                    st.error("Failed to combine audio with video.")
            else:
                st.error("Failed to generate translated audio.")
        except Exception as e:
            st.error(f"Error occurred: {e}")

elif input_mode == "Speech Input":
    st.subheader("🎙️ Record Your Voice")
    from audiorecorder import audiorecorder
    audio = audiorecorder("Click to record", "Click to stop recording")
    
    if len(audio) > 0:
        st.audio(audio.export().read(), format="audio/wav")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
            audio.export(temp_audio_file.name, format="wav")
            temp_audio_file_path = temp_audio_file.name

        input_text = transcribe_audio(temp_audio_file_path)
        os.remove(temp_audio_file_path)
        st.write(f"Original Transcribed Text:\n{input_text}")

        if input_text:
            source_lang_code = detect_language(input_text)
            target_lang_code = [k for k, v in list_supported_languages().items() if v == target_lang][0]

            translated_text = translate_text(input_text, target_lang_code, source_lang_code)
            translated_audio_path = save_translated_audio(translated_text, target_lang_code)

            if translated_audio_path:
                st.write("Translated audio generated successfully.")
                st.write(f"Translated Text:\n{translated_text}")
                st.audio(translated_audio_path, format='audio/mp3')
            else:
                st.error("Failed to generate translated audio.")
else:
    input_text = st.text_area("Enter text to translate")
    if input_text:
        st.subheader("Original Text")
        st.write(input_text)

        if input_lang_override != "Auto-detect":
            source_lang_code = [k for k, v in list_supported_languages().items() if v == input_lang_override][0]
        else:
            source_lang_code = detect_language(input_text)

        target_lang_code = [k for k, v in list_supported_languages().items() if v == target_lang][0]

        translated_text = translate_text(input_text, target_lang_code, source_lang_code)

        if translated_text:
            st.subheader(f"Translated Text ({get_full_language_name(target_lang_code)})")
            st.write(translated_text)

            audio_file = save_translated_audio(translated_text, target_lang_code)
            st.audio(audio_file, format='audio/mp3')
        else:
            st.error("Translation failed. Please try again.")
