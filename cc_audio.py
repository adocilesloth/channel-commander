import discord
import threading
import pyaudio
import time
import keyboard
from platform import system as OS

class audio_input():
    """Threaded audio input class"""

    def __init__(self, key):
        self.key = key
        self.in_channel = False
        self.running = True
        self.voice = None

        if OS() == 'Darwin':
            self.CHANNELS = 1
            self.FORMAT = pyaudio.paInt16
            self.CHUNK = 1920
        else:
            self.CHANNELS = 2
            self.FORMAT = pyaudio.paInt16
            self.CHUNK = 960
        self.RATE = 48000
        self.pAudio = pyaudio.PyAudio()

        #Run the input in a new thread
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def get_voice(self, voice):
        #Get VoiceChannel
        self.voice = voice

    def _callback(self, in_data, frame_count, time_info, flag):
        #Callback for getting audio input
        if self.voice is not None:
            #Send mic input to Discord
            self.voice.send_audio_packet(in_data)
        return (in_data, pyaudio.paContinue)

    def set_in_channel(self, in_channel):
        #bool for if in channel
        self.in_channel = in_channel

    def shutdown(self):
        #bool for shutting down the Thread
        self.running = False

    def run(self):
        print("Audio input at {0}Hz with {1} channels".format(self.RATE, self.CHANNELS))
        stream = self.pAudio.open(format=self.FORMAT,
                                channels=self.CHANNELS,
                                rate=self.RATE,
                                output=False,
                                input=True,
                                frames_per_buffer=self.CHUNK,
                                stream_callback=self._callback)
        stream.stop_stream()

        while self.running:
            #While running
            if keyboard.is_pressed(self.key) and self.in_channel:
                #If hotkey is pressed, start streaming
                stream.start_stream()
                while keyboard.is_pressed(self.key) and self.in_channel and self.running:
                    #While key is pressed, keep streaming
                    time.sleep(0.03)
                #Once key is nolonger pressed, stop streaming
                stream.stop_stream()
            time.sleep(0.03)

        #Once shutdown, stop streaming and close pAudio
        stream.close()
        self.pAudio.terminate()
