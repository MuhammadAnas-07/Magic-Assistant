# Voice Assistant Project

This is a simple voice assistant project written in Python. It can recognize spoken commands, respond to the user via speech synthesis, tell jokes, open websites, and provide the current time.

## Features

- **Speech Recognition:** Listens to user input and converts it into text.
- **Text-to-Speech:** Responds to user input by converting text into speech.
- **Jokes:** Can tell different types of jokes (Chuck Norris jokes, neutral jokes, etc.).
- **Website Opening:** Opens popular websites like Google, YouTube, Facebook, etc., when requested.
- **Time:** Tells the current time in a readable format.
- **Custom User Interaction:** Greets the user and responds to certain questions (e.g., "What is your name?" or "How old are you?").

## Requirements

To run this project, you need the following Python libraries:

- `speech_recognition`: For speech-to-text conversion.
- `pyttsx3`: For text-to-speech conversion.
- `pyjokes`: For generating jokes.
- `webbrowser`: To open websites in a browser.
- `re`: For regular expressions used in command matching.
- `datetime`: To fetch and format the current time.

You can install the required libraries using `pip`:

```bash
pip install speechrecognition pyttsx3 pyjokes
