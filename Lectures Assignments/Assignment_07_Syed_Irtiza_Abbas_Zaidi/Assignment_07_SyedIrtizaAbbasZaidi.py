import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("💬 Listening... 💬")
        audio = recognizer.listen(source)
        st.success("💬 Voice recorded successfully! 🔊")
        return audio

def convert_speech_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio, language="ur-PK")
        st.write(f" 🧠 Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError:
        st.error("Could not request results from Google Speech Recognition service.")
        return None

def generate_response(input_text):
    response_text = f"آپ نے کہا: {input_text}"
    return response_text

def convert_text_to_speech(text):
    tts = gTTS(text=text, lang="ur")
    return tts

def play_audio(tts):
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    audio = AudioSegment.from_file(audio_fp, format="mp3")
    play(audio)

def save_and_display_audio(tts):
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")

def main():
    st.title("🎙 Urdu Voice Assistant App 🔊")

    st.write("Click the button to record your voice in Urdu.")
    if st.button("Record Voice"):
        audio = record_voice()
        if audio:
            input_text = convert_speech_to_text(audio)
            if input_text:
                response_text = generate_response(input_text)
                st.write(f"Response: {response_text}")
                tts = convert_text_to_speech(response_text)
                save_and_display_audio(tts)
    
    st.header("👨‍💻 Developed by: SYED IRTIZA ABBAS ZAIDI")

if __name__ == "__main__":
    main()
