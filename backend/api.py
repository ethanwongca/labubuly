from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

voices = [{"name": "Default", "voice_id": "hO2yZ8lxM3axUxL8OeKX"},
          {"name": "Breathy", "voice_id": "HgyIHe81F3nXywNwkraY"},
          {"name": "Deep", "voice_id": "exxAZVMfY4Qs7F9CS1oN"},
          {"name": "Whiny", "voice_id": "chcMmmtY1cmQh2ye1oXi"},
          {"name": "Screech", "voice_id": "342hpGp7PKo7DsTTVSdr"}]

class VoiceAPI(BaseModel):
    name: str

@app.post("/selected_voice")
def select_voice(selected_voice: VoiceAPI):
    name = selected_voice.name
    voice_id = None 
    for voice_dict in voices:
        if voice_dict["name"] == name:
            voice_id = voice_dict["voice_id"]
            break

    if not voice_id:
        raise HTTPException(status_code=404, detail="Voice name not found")
    
    return voice_id