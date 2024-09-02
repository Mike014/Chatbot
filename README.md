# ChatBot

This repository contains the prototype of a ChatBot designed for audio playback and other audio-related functionalities in both video games and other applications.

**SoundBot** is a modular ChatBot that leverages **Digital Signal Processing (DSP)** to generate sounds based on voice commands. DSP involves the manipulation of digital signals, such as audio, to enhance or analyze them. This allows for the creation of a rich and interactive audio experience by processing and transforming sound in real-time.

### Key Features

- **Bias_Handler** and **Sentiment_Analysis** modules currently have a bug.
- Utilizes the **NLTK** (Natural Language Toolkit) and **regex** (regular expressions) for Natural Language Processing (NLP) and speech recognition.
- Generates sounds based on voice commands, making it a versatile tool for various applications.

### Directory Structure

- **Modules**: Contains the different modules of the project.
- **Test**: Includes various tests for different aspects of the prototype.
- **Main.py**: The primary Python file needed to run the ChatBot, located in the `Modules` directory.

### Steps to Download and Set Up the Project

1. **Install Git (if not already installed):**
   - Go to the official [Git website](https://git-scm.com/).
   - Download and install Git following the instructions for your operating system.

2. **Clone the Repository:**
   - Open your terminal (on macOS or Linux) or command prompt (on Windows).
   - Run the following command to clone the repository:
     ```bash
     git clone https://github.com/Mike014/Chatbot.git
     ```
   - This command will create a local copy of the repository in your current directory.

3. **Navigate to the Project Directory:**
   - Go to the project folder you just cloned:
     ```bash
     cd Chatbot
     ```

4. **Install Dependencies:**
   - Ensure you have Python installed. You may also need to install dependencies such as NLTK and any other required libraries. You can typically do this using `pip`:
     ```bash
     pip install nltk
     ```

5. **Run the ChatBot:**
   - Navigate to the `Modules` directory:
     ```bash
     cd Modules
     ```
   - Execute the main Python file to start the ChatBot:
     ```bash
     python Main.py
     ```

6. **Explore and Test:**
   - Check out the various modules and test different aspects of the prototype as described in the `Test` directory.

### Additional Notes

- If you encounter issues, make sure you have all the necessary dependencies installed and check for any specific installation instructions in the repository.
- Refer to the repository's README file for more details and updates.

## Video on YouTube

### Video 1
[![Video 1](https://img.youtube.com/vi/RP8IiiImbO0/0.jpg)](https://www.youtube.com/watch?v=RP8IiiImbO0&list=PLgKASgLUSpNaUfSrkMirwRU2skzNGbnRs&index=52)
In the video, you'll see how, given a user input, the chatbot interprets the user's intent and matches the input value to one of the keys in the chord dictionary. For instance, if the user requests a "C major", the chatbot locates this chord in the dictionary and generates the sound wave corresponding to the specified frequencies.

### Video 2
[![Video 2](https://img.youtube.com/vi/tjzaMJyNJys/0.jpg)](https://www.youtube.com/watch?v=tjzaMJyNJys&list=PLgKASgLUSpNaUfSrkMirwRU2skzNGbnRs&index=48)
This application uses the pygame, speech_recognition, and pydub libraries to play a Pink Noise audio file and control its stereo positioning, or 'panning', through voice commands. For the best experience, put on your headphones and listen as the user speaks commands like "right", "left", "center", "center right", and "center left" to control the stereo position of the sound. Saying "right" pans the sound entirely to the right channel, while "left" pans it to the left. Saying "center" balances the sound equally between both channels.

For more information, visit the repository: [GitHub - ChatBot](https://github.com/Mike014/Chatbot.git)
