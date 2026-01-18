import pyaudio
import wave

class AudioRecorder:
    def __init__(self, rate=16000, chunk=1024):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = rate
        self.chunk = chunk
        
        self.audio_interface = None
        self.audio_stream = None
        self.audio_active = False
        self.frames = []

    def start_audio_stream(self):
        if self.audio_active:
            return

        self.audio_interface = pyaudio.PyAudio()
        self.frames = []

        self.audio_stream = self.audio_interface.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )

        self.audio_active = True
        print(f"Microphone started at {self.rate}Hz")

    def stop_audio_stream(self):
        if not self.audio_active:
            return
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.audio_interface.terminate()
        self.audio_active = False