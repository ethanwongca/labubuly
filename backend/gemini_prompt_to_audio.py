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

    sentence = "How do I look today, give me a compliment"

    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=f"""Your persona is a high energetic child. Like a labubu you see on Youtube
                    Your responses should be flirty and playful
                    Give an answer to the following sentence: {sentence}
                    Limit your response to one sentence."""
    )
    
    audio = elevenlabs.text_to_dialogue.convert(
        inputs=[
            {
                "text": f"{response.text}",
                "voice_id": "hO2yZ8lxM3axUxL8OeKX"
            }
        ]
    )

    play(audio)