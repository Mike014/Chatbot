## Voice-Controlled Music Player: A Python Chatbot in Action

- Voice-commanded music playback chatbot built with Python. This script showcases the integration of speech recognition and audio playback functionalities.

# Key Features: 
- Voice-Activated Music Playback: Just say the song name, and the chatbot plays it for you.
- Stop Playback on Command: A simple voice command can stop the music anytime.
- Smart Song Search: Finds the best match for your song request within a specified directory.

# Technologies Used:
- pygame: For seamless audio playback.
- speech_recognition: Powers the voice command feature, converting spoken words into text.
- threading: Ensures music playback and voice listening run concurrently without hitches.
- os and re: Assist in file handling and command parsing.

# How It Works:
- Initialization: Sets up the audio playback environment.
- Continuous Listening: Enters a loop to listen for voice commands like "play [song name]" or "stop".
- Action Execution: Based on the recognized command, it either plays the requested song or stops the current playback.
- Song Search: Searches for the best match for the requested song in the specified directory and plays it.

This project is a testament to the power of combining different Python libraries to create interactive applications. Stay tuned for more updates!