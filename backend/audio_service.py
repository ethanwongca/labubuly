import os
from google import genai
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

class TexttoAudioService:
    def __init__(self):
        gemini_key = os.getenv("GEMINI_API_KEY")
        eleven_key = os.getenv("ELEVENLABS_API_KEY")
        
        self.gemini_client = genai.Client(api_key=gemini_key)
        self.elevenlabs_client = ElevenLabs(api_key=eleven_key)

    def prompt_to_audio(self, prompt, speaker_id):
        response = self.gemini_client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=f"""Your persona is a high energetic child named Labubu.
                        Your responses are playful, slightly flirty, and very cute.
                        Answer this: {prompt}
                        Limit to ONE short sentence."""
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