from google import genai
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

load_dotenv()
elevenlabs = ElevenLabs(
api_key=os.getenv("ELEVENLABS_API_KEY"),
)

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

voices = [{"name": "Default", "voice_id": "hO2yZ8lxM3axUxL8OeKX"},
          {"name": "Breathy", "voice_id": "HgyIHe81F3nXywNwkraY"},
          {"name": "Deep", "voice_id": "exxAZVMfY4Qs7F9CS1oN"},
          {"name": "Whiny", "voice_id": "chcMmmtY1cmQh2ye1oXi"},
           {"name": "Screech", "voice_id": "342hpGp7PKo7DsTTVSdr"}]

@app.get("/voices")
def get_voices():
    return voices

class Voice(BaseModel):
        name: str
        voice_id: str

selected_voice_id = "NhO2yZ8lxM3axUxL8OeKX" # onky works for one user at a time
# set as default just in case, but frontend should send the default voice back upon start too
@app.post("/selected_voice")
def select_voice(selected_voice: Voice):
    global selected_voice_id 
    selected_voice_id  = selected_voice.voice_id
    return f"selected: {selected_voice.name}"

     
    


if __name__ == "__main__":

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
                "voice_id": selected_voice_id
            }
        ]
    )

    play(audio)