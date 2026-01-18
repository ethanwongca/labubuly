from google import genai
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

class TexttoAudioService:
    def __init__(self):
        self.gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.elevenlabs_client = ElevenLabs(api_key=os.getenv("LEVENLABS_API_KEY"))

    def prompt_to_audio(self, prompt, speaker_id):
        response = self.gemini_client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=f"""Your persona is a high energetic child. Like a labubu you see on Youtube
                    Your responses should be flirty and playful
                    Give an answer to the following sentence: {prompt}
                    Limit your response to one sentence."""
        )

        audio = self.elevenlabs_client.text_to_dialogue.convert(
        inputs=[
            {
                "text": f"{response.text}",
                "voice_id": speaker_id
            }
        ]
        )

        return audio