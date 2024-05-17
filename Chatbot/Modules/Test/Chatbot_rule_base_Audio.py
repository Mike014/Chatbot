# -*- coding: utf-8 -*-
import os
import re
import pygame
import speech_recognition as sr
import threading

def initialize_pygame():
    pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=512)

def play_song(file_path):
    def play():
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        else:
            print("A song is already playing.")
    threading.Thread(target=play).start()

def stop_song():
    pygame.mixer.music.stop()
    print("Song stopped.")

def find_best_match(directory, keywords):
    normalized_keywords = keywords.lower().split()
    best_match = None
    max_matches = 0
    for file in os.listdir(directory):
        file_without_extension = os.path.splitext(file)[0]
        file_words = file_without_extension.lower().replace("_", " ").split()
        matches = sum(word in file_words for word in normalized_keywords)
        if matches > max_matches:
            best_match = file
            max_matches = matches
    return os.path.join(directory, best_match) if best_match else None

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  
        print("Listening for command...")
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=6)
            return r.recognize_google(audio, language='en-EN')
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start. Please try again.")
            return None 

def main():
    directory = "D:\\Playlist Musica"
    initialize_pygame()
    while True:
        command = listen_for_command()
        if command:
            if "stop" in command.lower():
                stop_song()
                continue
            match = re.search(r"play\s(.+)", command.lower())
            if match:
                keywords = match.group(1)
                song_path = find_best_match(directory, keywords)
                if song_path:
                    print(f"Playing the song: {os.path.basename(song_path).replace('_', ' ')}")
                    play_song(song_path)
                else:
                    print("No matching song found. Try different keywords.")
            else:
                print("Command not recognized. Please say 'play' followed by the song title.")
        else:
            print("No command recognized. Please try again.")

if __name__ == "__main__":
    main()








