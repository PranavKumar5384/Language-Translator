import moviepy.editor as mp
from gtts import gTTS


def extract_audio_from_video(video_path, output_audio_path="extracted_audio.mp3"):
    """Extract audio from the given video file."""
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    return output_audio_path


def save_translated_audio(text, lang_code, output_path="tts_output.mp3"):
    """Convert translated text to speech and save as audio."""
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)
    return output_path


def combine_audio_with_video(video_path, audio_path, output_path="final_output.mp4"):
    """Combine new audio with the original video."""
    video_clip = mp.VideoFileClip(video_path).without_audio()
    audio_clip = mp.AudioFileClip(audio_path)
    final_video = video_clip.set_audio(audio_clip)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
