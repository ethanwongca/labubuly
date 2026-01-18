import time
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAV_FILENAME = "audio.wav"
RECORD_SECONDS = 5

audio_stream = None
audio_interface = None
audio_active = False
frames = []

def start_audio_stream():
  global audio_stream, audio_interface, audio_active, frames

  if audio_active:
    return

  audio_interface = pyaudio.PyAudio()
  frames = []

  audio_stream = audio_interface.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
  )

  audio_active = True
  print("Audio stream started")

def stop_audio_stream():
  global audio_stream, audio_interface, audio_active, frames

  if not audio_active:
    return

  try:
    audio_stream.stop_stream()
    audio_stream.close()
    audio_interface.terminate()
    audio_active = False

    print("Audio stream stopped")

    with wave.open(WAV_FILENAME, "wb") as wf:
      wf.setnchannels(CHANNELS)
      wf.setsampwidth(audio_interface.get_sample_size(FORMAT))
      wf.setframerate(RATE)
      wf.writeframes(b''.join(frames))
    
    print("Audio file saved")
  except Exception as e:
    print(f"Error stopping audio stream: {e}")

start_audio_stream()

start_time = time.time()

while time.time() - start_time < RECORD_SECONDS:
  data = audio_stream.read(CHUNK)
  frames.append(data)

stop_audio_stream()