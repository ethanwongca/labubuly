import os
# import signal
import time
from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector
from eff_word_net.audio_processing import Resnet50_Arc_loss
# from elevenlabs.client import ElevenLabs
# from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
# from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# elevenlabs=ElevenLabs()
api_key=os.getenv("ELEVENLABS_API_KEY")
# agent_id=os.getenv("ELEVENLABS_AGENT_ID")

base_model = Resnet50_Arc_loss()

hotword_detector = HotwordDetector(
  hotword="hey_eleven",
  model = base_model,
  reference_file=os.path.join("hotword_refs", "hey_eleven_ref.json"),
  threshold=0.7,
  relaxation_time=2
)

mic_stream = None
audio_active = False

def start_audio_stream():
  # Start mic audio stream
  global mic_stream, audio_active

  if audio_active:
    return
  
  mic_stream = SimpleMicStream(
    window_length_secs=1.5,
    sliding_window_secs=0.75,
  )

  mic_stream.start_stream()
  audio_active = True
  print("Microphone stream started")

def stop_audio_stream():
  global mic_stream, audio_active

  try:
    if mic_stream:
      mic_stream = None
      audio_active = False
      print("Microphone stream stopped")
    except Exception as e:
      print(f"Error stopping microphone stream: {e}")

def wait_for_hotword():
  global mic_stream

  print("Say 'Hey Eleven' to start audio stream")

  mic_stream = (
    window_length_secs=1.5,
    sliding_window_secs=0.75,
  )

  mic_stream.start_stream()

  while True:
    frame = mic_stream.getFrame()
    result = hotword_detector.scoreFrame(frame)

    if result and result["match"]:
      print("Hotword detected")
      stop_audio_stream()
      start_audio_stream()
      break

wait_for_hotword()
time.sleep(5)
stop_audio_stream()