#STT-TTS
##Speech to Text - Translate - Text to Speech

This **Audio Translator** application is a simple tool that allows users to convert spoken language into text, translate it into a target language, and then read it out loud using text-to-speech. The app supports various languages and makes use of Google APIs for speech recognition, translation, and speech synthesis.

## Features
- **Speech-to-Text**: Capture speech and convert it into text.
- **Translation**: Translate the recognized speech into any target language.
- **Text-to-Speech**: Convert the translated text into speech and play it aloud.
- **Language Code Guide**: View the language codes for various languages supported by the translation service.
- **Interactive GUI**: Easy-to-use interface with clear buttons and instructions.

## Requirements

Make sure you have the following libraries installed:

- **Tkinter**: For creating the graphical user interface.
- **gTTS (Google Text-to-Speech)**: To convert text into speech.
- **googletrans**: For translating text to the target language.
- **SpeechRecognition**: To capture and convert speech to text.
- **PyAudio**: To enable microphone functionality for speech recognition.

You can install the required libraries using pip:

```bash
pip install gTTS googletrans SpeechRecognition pyaudio
```


**Note: pyaudio might require additional steps to install on certain systems. For more information, refer to the official documentation: PyAudio Installation.**

## How to Use
### Step 1: Open the Application
-Run the Python script audio_translator.py to launch the GUI.
### Step 2: Input Target Language Code
-In the Target Language Code field, enter the desired language code (e.g., 'es' for Spanish or 'fr' for French).
### Step 3: View Language Code Guide
-Click the Language Code Guide button to view a table of common language codes supported by the translation API.
### Step 4: Start Recording
-Click Start Recording to begin recording your speech. Speak clearly into the microphone. Once the speech is captured, it will be converted into text and displayed in the Recognized Text field.
### Step 5: Translation and Text-to-Speech
-The recognized text will be translated to the specified target language, and the translated text will be read out loud by the application.
### Step 6: Exit
-Click Exit to close the application.

## GUI Overview
-**Target Language Code Field**: Input the language code for translation.
-**Language Code Guide**: Button to open a window displaying language codes.
-**Start Recording**: Button to start capturing speech.
-**Status**: Displays the current status of the application (e.g., "Listening...", "Speech recognized!").
-**Recognized Text**: Displays the text recognized from the speech.
-**Exit**: Button to close the application.
## License
-This project is open-source and available under the MIT License.
