# example.py
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_dialogue.convert(
    inputs=[
        {
            "text": "labubu",
            "voice_id": "eppqEXVumQ3CfdndcIBd",
        },
        {
            "text": "labubu",
            "voice_id": "hO2yZ8lxM3axUxL8OeKX",
        }
    ]
)

play(audio)
