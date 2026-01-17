from google import genai
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

if __name__ == "__main__":
    load_dotenv()
    elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    )
    
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Slay Queen, how's you're day"
    )
    
    audio = elevenlabs.text_to_dialogue.convert(
        inputs=[
            {
                "text": f"{response.text}",
                "voice_id": "JBFqnCBsd6RMkjVDRZzb"
            }
        ]
    )

    play(audio)