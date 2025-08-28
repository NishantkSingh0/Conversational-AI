from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
client = OpenAI(api_key=os.getenv("OpenAI"))

def SpeechToText(buffer):
    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",  
        file=buffer,
        response_format="text"
    )
    return transcription 


def TextToSpeech(text):
    """Converts Raw English text to Speech"""
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        response_format="wav",
        input=text
    )
    return response