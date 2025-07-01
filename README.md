**🌍 Language Translator**

This is a Streamlit web application project that allows users to translate words or spoken content from one language to another with the help of AI-driven transcription, translation, and text-to-speech technologies. It takes inputs from audio, video, speech, and text, and gives outputs in the form of translated audio or even dubbed video..

**🚀 Features**

🎥 Upload audio/videos and translate what was being spoken

🎙️ Speak into your microphone and receive voice outputs of translations

📝 Write text and listen to it translated into another language

🌐 Automatic detection of language or selection

📼 Creates a new video with translated audio for video posts

**🛠️ Tech Stack**

Frontend: Streamlit

Transcription: OpenAI Whisper

Translation: Google Translate API (googletrans)

TTS (Text-to-Speech): gTTS (Google Text-to-Speech)

Video Editing: moviepy

**📦 Installation**

#1. Clone the repo:\n

#git clone https://github.com/yourusername/Language-Translator.git

cd Language-Translator

#2. Create virtual environment:

python -m venv venv

source venv/bin/activate    # on Linux/macOS

venv\Scripts\activate       # on Windows

3. Install dependencies:
   
pip install -r requirements.txt

**▶️ Usage**

#Run the app using Streamlit:

streamlit run app.py

Then open the local URL provided (e.g., http://localhost:8501) in your browser.

**📁 Project Structure**

├── app.py              
├── transcribe.py         
├── translate.py         
├── tts.py                
├── utils.py             
├── video_utils.py        
├── requirements.txt 

**✅ Requirements**

Python 3.11

ffmpeg (for audio/video processing, required by moviepy & pydub)

Install via: sudo apt install ffmpeg or brew install ffmpeg or from https://ffmpeg.org

**📌 Notes**

OpenAI Whisper model runs locally; no API key required.

googletrans sometimes fails due to rate-limiting—best effort translation.

TTS voice is synthetic and generated via gTTS.
