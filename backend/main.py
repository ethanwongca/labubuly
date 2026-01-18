import asyncio
import websockets
import json
import base64
import os
import time
from dotenv import load_dotenv
from gpiozero import Button

from audio_to_stream import AudioRecorder
from audio_service import TexttoAudioService
from six_seven import SixSeven
from elevenlabs.play import play

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "exxAZVMfY4Qs7F9CS1oN" 
MODEL_ID = "scribe_v2_realtime"
WS_URL = f"wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id={MODEL_ID}"

running = False

async def main():
    global running

    recorder = AudioRecorder(rate=16000)
    ai_service = TexttoAudioService()
    six_seven = SixSeven()

    recorder.start_audio_stream()
    
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    
    async with websockets.connect(WS_URL, extra_headers=headers) as ws:
        # Config to ensure fast processing
        config_message = {
            "message_type": "session_update",
            "config": {
                "vad_silence_threshold_secs": 0.5,
                "language_code": "en"
            }
        }
        await ws.send(json.dumps(config_message))
        
        print("--- Labubu is listening for 5 seconds... ---")
        start_time = time.time()

        async def send_audio():
            """Sends audio for exactly 5 seconds then stops mic."""
            try:
                while recorder.audio_active and (time.time() - start_time < 5):
                    # Show a countdown in the terminal
                    remaining = 5 - int(time.time() - start_time)
                    print(f"Time left: {remaining}s | Labubu is recording...", end="\r")
                    
                    data = recorder.audio_stream.read(recorder.chunk, exception_on_overflow=False)
                    message = {
                        "message_type": "input_audio_chunk",
                        "audio_base_64": base64.b64encode(data).decode("utf-8")
                    }
                    await ws.send(json.dumps(message))
                    await asyncio.sleep(0.01)
                
                # TELL SERVER WE ARE DONE: This forces the transcript to finalize
                end_message = {
                    "message_type": "input_audio_chunk",
                    "audio_base_64": base64.b64encode(b"").decode("utf-8"), # Empty chunk
                    "commit": True # Force the server to process immediately
                }
                await ws.send(json.dumps(end_message))
                
                print("\n--- Mic Off! Processing your request... ---")
                recorder.stop_audio_stream() 
            except Exception as e:
                print(f"Streaming Error: {e}")

        async def receive_transcripts():
            """Waits as long as necessary for the final transcript and AI reply."""
            async for message in ws:
                response = json.loads(message)
                
                # We only care about the final committed transcript now
                if response.get("message_type") == "committed_transcript":
                    user_text = response.get("text")
                    if user_text.strip():
                        print(f"You said: {user_text}")
                        print("Labubu is thinking...")
                        
                        try:
                            # This part can take a few seconds, and that's okay!
                            audio_output = ai_service.prompt_to_audio(user_text, VOICE_ID)
                            print("Labubu is talking! 💬")
                            play(audio_output)
                        except Exception as e:
                            print(f"AI Service Error: {e}")
                    
                    # Return ends this function, allowing the program to close
                    return 

        # We run them together. The program stays open until BOTH are finished.
        await asyncio.gather(send_audio(), receive_transcripts())
        print("Pipeline complete. Goodbye!")
        await six_seven.six_seven()
        running = False

if __name__ == "__main__":
    try:
        button = Button(22)

        while True:
            button.wait_for_press()
            button.wait_for_release()

            time.sleep(0.2)

            if not running:
                running = True
                asyncio.run(main())

    except KeyboardInterrupt:
        print("\nLabubu is going to sleep! Bye bye!")
        running = False