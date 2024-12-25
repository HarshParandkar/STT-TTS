import tkinter as tk
from tkinter import messagebox, Toplevel
import threading
from gtts import gTTS
from googletrans import Translator
import os
import speech_recognition as sr

# Speech-to-Text Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            status_label.config(text="Listening...")
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio)
            status_label.config(text="Speech recognized!")
            return text
        except:
            status_label.config(text="Failed to recognize speech.")
            return None

# Translation Function
def translate_text(input_text, target_language):
    translator = Translator()
    translated = translator.translate(input_text, dest=target_language)
    return translated.text

# Text-to-Speech Function
def text_to_speech(translated_text, language):
    tts = gTTS(text=translated_text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

# Main Function
def process_audio():
    try:
        # Speech-to-Text
        input_text = speech_to_text()
        if input_text:
            text_entry.delete(0, tk.END)
            text_entry.insert(0, input_text)

            # Translation
            target_language = lang_entry.get()
            translated_text = translate_text(input_text, target_language)

            # Text-to-Speech
            text_to_speech(translated_text, target_language)
        else:
            messagebox.showerror("Error", "Speech recognition failed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Language Code Guide Window
def open_language_code_guide():
    guide_window = Toplevel(root)
    guide_window.title("Language Code Guide")
    guide_window.geometry("500x400")

    tk.Label(guide_window, text="Common Language Codes", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Creating a table of language pairs
    guide_frame = tk.Frame(guide_window)
    guide_frame.pack(pady=5)

    columns = ['Language', 'Code', 'Language', 'Code']
    for i, column in enumerate(columns):
        tk.Label(guide_frame, text=column, font=("Arial", 12, "bold"), borderwidth=1, relief="solid", padx=10, pady=5).grid(row=0, column=i, sticky='nsew')

    guide_data = [
        ("Afrikaans", "af", "Italian", "it"),
        ("Arabic", "ar", "Japanese", "ja"),
        ("Bengali", "bn", "Korean", "ko"),
        ("Bulgarian", "bg", "Latin", "la"),
        ("Catalan", "ca", "Malay", "ms"),
        ("Chinese (Simplified)", "zh-CN", "Marathi", "mr"),
        ("Chinese (Traditional)", "zh-TW", "Norwegian", "no"),
        ("Croatian", "hr", "Persian", "fa"),
        ("Czech", "cs", "Polish", "pl"),
        ("Danish", "da", "Portuguese", "pt"),
        ("Dutch", "nl", "Punjabi", "pa"),
        ("English", "en", "Romanian", "ro"),
        ("Estonian", "et", "Russian", "ru"),
        ("Filipino", "tl", "Serbian", "sr"),
        ("Finnish", "fi", "Spanish", "es"),
        ("French", "fr", "Swahili", "sw"),
        ("German", "de", "Swedish", "sv"),
        ("Greek", "el", "Tamil", "ta"),
        ("Gujarati", "gu", "Telugu", "te"),
        ("Hebrew", "iw", "Thai", "th"),
        ("Hindi", "hi", "Turkish", "tr"),
        ("Hungarian", "hu", "Ukrainian", "uk"),
        ("Icelandic", "is", "Urdu", "ur"),
        ("Indonesian", "id", "Vietnamese", "vi"),
    ]

    for row_num, row_data in enumerate(guide_data, start=1):
        for col_num, item in enumerate(row_data):
            tk.Label(guide_frame, text=item, font=("Arial", 10), borderwidth=1, relief="solid", padx=10, pady=5).grid(row=row_num, column=col_num, sticky='nsew')

    for i in range(4):
        guide_frame.grid_columnconfigure(i, weight=1)
    for i in range(len(guide_data) + 1):
        guide_frame.grid_rowconfigure(i, weight=1)
    
    close_button = tk.Button(guide_window, text="Close", font=("Arial", 12), command=guide_window.destroy)
    close_button.pack(pady=10)

# GUI Setup
root = tk.Tk()
root.title("Audio Translator")
root.geometry("450x550")
root.resizable(False, False)

# Styling Variables
font_style = ("Arial", 12)

# Top Heading
tk.Label(root, text="Audio Translator", font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

# Steps Label
steps_text = """
Steps to Use the Application:
1. Enter the target language code (e.g., 'es' for Spanish).
2. Click 'Language Code Guide' to view the language codes.
3. Click 'Start Recording' to begin recording your speech.
4. The recognized text will appear below.
5. The translated text will be spoken aloud after processing.
"""
tk.Label(root, text=steps_text, font=("Arial", 10), justify="left").pack(pady=5)

# Language Code Field and Guide Button moved to the top
tk.Label(root, text="Target Language Code (e.g., 'es', 'fr')", font=font_style).pack(pady=5)
lang_entry = tk.Entry(root, font=font_style)
lang_entry.pack(pady=5)

# Guide Button Below Language Code Field
guide_button = tk.Button(root, text="Language Code Guide", font=("Arial", 12), command=open_language_code_guide)
guide_button.pack(pady=10)

# Start Recording Button
start_button = tk.Button(root, text="Start Recording", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=lambda: threading.Thread(target=process_audio).start())
start_button.pack(pady=15, fill="x")

# Status Label
status_label = tk.Label(root, text="Status: Idle", font=("Arial", 10, "italic"), fg="gray")
status_label.pack(pady=10)

# Recognized Text
tk.Label(root, text="Recognized Text", font=font_style).pack(pady=5)
text_entry = tk.Entry(root, font=font_style, width=50)
text_entry.pack(pady=5)

# Exit Button at the End
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit, bg="#FF6347", fg="white")
exit_button.pack(pady=10, fill="x")

# Run the GUI
root.mainloop()
