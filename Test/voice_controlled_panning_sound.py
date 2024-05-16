# -*- coding: utf-8 -*-
import pygame
import speech_recognition as sr
from pydub import AudioSegment

AUDIO_FILE_PATH = "C:\\Users\\PC\\Desktop\\Pink Noise\\Pink Noise.wav"

class SoundPlayer:
    def __init__(self):
        self.sound = AudioSegment.from_file(AUDIO_FILE_PATH)
        self.pygame_sound = None

    def play_sound(self, pan_value):
        panned_sound = self.sound.pan(pan_value)

        raw_audio_data = panned_sound.raw_data
        num_channels = panned_sound.channels
        bytes_per_sample = panned_sound.sample_width
        sample_rate = panned_sound.frame_rate

        pygame.mixer.init(sample_rate, -8 * bytes_per_sample, num_channels)
        self.pygame_sound = pygame.mixer.Sound(buffer=raw_audio_data)
        self.pygame_sound.play()

    def stop_sound(self):
        if self.pygame_sound is not None:
            self.pygame_sound.stop()

def recognize_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='it-IT')
        print("You said: " + command)
        command = command.replace("-", " ")  # Replace hyphens with spaces
        return command
    except (sr.UnknownValueError, sr.RequestError) as e:
        print(f"Error: {str(e)}")
        return None

sound_player = SoundPlayer()

command_to_pan_value = {
    "destra": 1,
    "sinistra": -1,
    "centro": 0,
    "centro destra": 0.5,
    "centro sinistra": -0.5
}

while True:
    command = recognize_command()
    if command in command_to_pan_value:
        sound_player.stop_sound()
        sound_player.play_sound(command_to_pan_value[command])
    elif command == "stop":
        sound_player.stop_sound()
        break
    else:
        print("Invalid command")



