

# import os
# import pyautogui
# import subprocess
# import webbrowser
# import pyttsx3
# import requests
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow JavaScript requests

# # Initialize Text-to-Speech
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Set female voice

# def speak(text):
#     """Convert text to speech."""
#     engine.say(text)
#     engine.runAndWait()

# def fetch_news():
#     """Fetch the latest news from an API."""
#     try:
#         url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY"
#         response = requests.get(url).json()
#         articles = response.get("articles", [])[:5]
#         news_headlines = [article["title"] for article in articles]
#         return news_headlines
#     except Exception as e:
#         return ["Failed to fetch news."]

# @app.route('/process-command', methods=['POST'])
# def process_command():
#     """Handles voice commands from the frontend."""
#     data = request.json
#     command = data.get("command", "").lower()

#     print(f"Received Command: {command}")  # Debugging log
#     response = ""

#     # **Open Websites**
#     website_commands = {
    #     "youtube": "https://www.youtube.com",
    #     "google": "https://www.google.com",
    #     "gmail": "https://mail.google.com",
    #     "facebook": "https://www.facebook.com",
    #     "instagram": "https://www.instagram.com",
    #     "twitter": "https://twitter.com",
    #     "reddit": "https://www.reddit.com",
    #     "linkedin": "https://www.linkedin.com",
    #     "amazon": "https://www.amazon.com",
    #     "netflix": "https://www.netflix.com",
    #     "spotify": "https://open.spotify.com",
    #     "github": "https://github.com",
    #     "stackoverflow": "https://stackoverflow.com",
    #     "quora": "https://www.quora.com",
    #     "wikipedia": "https://www.wikipedia.org",
    #     "discord": "https://discord.com",
    #     "whatsapp web": "https://web.whatsapp.com",
    #     "telegram web": "https://web.telegram.org",
    #     "udemy": "https://www.udemy.com",
    #     "coursera": "https://www.coursera.org",
    #     "zoom": "https://zoom.us",
    #     "google maps": "https://www.google.com/maps",
    #     "pinterest": "https://www.pinterest.com",
    #     "twitch": "https://www.twitch.tv",
    #     "apple": "https://www.apple.com",
    #     "microsoft": "https://www.microsoft.com",
    #     "yahoo": "https://www.yahoo.com",
    #     "bbc news": "https://www.bbc.com/news",
    #     "cnn": "https://www.cnn.com"
    # }

#     for site, url in website_commands.items():
#         if f"open {site}" in command:
#             webbrowser.open(url)
#             response = f"Opening {site.capitalize()}."
#             break

#     # **Open System Apps**
#     system_apps = {
#         "notepad": "notepad.exe",
#         "calculator": "calc.exe",
#         "word": "start winword",
#         "excel": "start excel",
#         "powerpoint": "start powerpnt",
#         "command prompt": "cmd.exe",
#         "file explorer": "explorer.exe",
#         "spotify": "spotify.exe",
#         "chrome": "start chrome",
#         "spotify": "spotify.exe",
#         "chrome": "start chrome",
#         "edge": "start msedge",
#         "vlc": "start vlc",
#         "paint": "mspaint.exe",
#         "photos": "start microsoft.photos",
#         "zoom": "start zoom"
#     }
    

#     for app_name, app_command in system_apps.items():
#         if f"open {app_name}" in command:
#             try:
#                 os.system(app_command)
#                 response = f"Opening {app_name.capitalize()}."
#             except Exception as e:
#                 response = f"Error opening {app_name}."
#             break

#     # **Control Notepad & Other Apps**
#     if "new file" in command:
#         pyautogui.hotkey("ctrl", "n")  # Create a new file
#         response = "Created a new file."

#     elif "save file" in command:
#         pyautogui.hotkey("ctrl", "s")  # Save file
#         response = "Saving file."

#     elif "close" in command:
#         pyautogui.hotkey("alt", "f4")  # Close window
#         response = "Closing the application."

#     elif "copy" in command:
#         pyautogui.hotkey("ctrl", "c")  # Copy
#         response = "Copied text."

#     elif "paste" in command:
#         pyautogui.hotkey("ctrl", "v")  # Paste
#         response = "Pasted text."

#     # **Fetch News**
#     elif "get news" in command or "latest news" in command:
#         news_headlines = fetch_news()
#         response = "Here are the latest news headlines:\n" + "\n".join(news_headlines)

        

#     # Default response if command is not recognized
#     if not response:
#         response = "Sorry, I didn't understand that."

#     # Speak the response
#     speak(response)

#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True)

import os
import time
import pyautogui
import subprocess
import webbrowser
import pyttsx3
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow JavaScript requests

# Initialize Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set female voice

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def fetch_news():
    """Fetch the latest news from an API."""
    try:
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY"
        response = requests.get(url).json()
        articles = response.get("articles", [])[:5]
        news_headlines = [article["title"] for article in articles]
        return news_headlines
    except Exception as e:
        return ["Failed to fetch news."]

def start_windows_dictation():
    """Start Windows built-in speech-to-text dictation (Win + H)."""
    time.sleep(2)  # Wait for the user to switch to the app
    pyautogui.hotkey("win", "h")  # Press Win + H to start dictation
    speak("Dictation started. Start speaking.")

@app.route('/process-command', methods=['POST'])
def process_command():
    """Handles voice commands from the frontend."""
    data = request.json
    command = data.get("command", "").lower()

    print(f"Received Command: {command}")  # Debugging log
    response = ""

    # **Open Websites**
    website_commands =  {

    "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://twitter.com",
        "reddit": "https://www.reddit.com",
        "linkedin": "https://www.linkedin.com",
        "amazon": "https://www.amazon.com",
        "netflix": "https://www.netflix.com",
        "spotify": "https://open.spotify.com",
        "github": "https://github.com",
        "stackoverflow": "https://stackoverflow.com",
        "quora": "https://www.quora.com",
        "wikipedia": "https://www.wikipedia.org",
        "discord": "https://discord.com",
        "whatsapp web": "https://web.whatsapp.com",
        "telegram web": "https://web.telegram.org",
        "udemy": "https://www.udemy.com",
        "coursera": "https://www.coursera.org",
        "zoom": "https://zoom.us",
        "google maps": "https://www.google.com/maps",
        "pinterest": "https://www.pinterest.com",
        "twitch": "https://www.twitch.tv",
        "apple": "https://www.apple.com",
        "microsoft": "https://www.microsoft.com",
        "yahoo": "https://www.yahoo.com",
        "bbc news": "https://www.bbc.com/news",
        "cnn": "https://www.cnn.com",
        "chat gpt": "https://chatgpt.com/"
    }


    for site, url in website_commands.items():
        if f"open {site}" in command:
            webbrowser.open(url)
            response = f"Opening {site.capitalize()}."
            break

    # **Open System Apps**
    system_apps = {
            "notepad": "notepad.exe",
        "calculator": "calc.exe",
      "word": "start winword",
         "excel": "start excel",
         "powerpoint": "start powerpnt",
        "command prompt": "cmd.exe",
         "file explorer": "explorer.exe",
         "spotify": "spotify.exe",
         "chrome": "start chrome",
         "spotify": "spotify.exe",
         "chrome": "start chrome",
         "edge": "start msedge",      
    "vlc": "start vlc",
         "paint": "mspaint.exe",
        "photos": "start microsoft.photos",
         "zoom": "start zoom"}

    for app_name, app_command in system_apps.items():
        if f"open {app_name}" in command:
            try:
                os.system(app_command)
                response = f"Opening {app_name.capitalize()}."
            except Exception as e:
                response = f"Error opening {app_name}."
            break

    # **Control Notepad & Other Apps**
    if "new file" in command:
        pyautogui.hotkey("ctrl", "n")  # Create a new file
        response = "Created a new file."

    elif "save file" in command:
        pyautogui.hotkey("ctrl", "s")  # Save file
        response = "Saving file."

    elif "close" in command:
        pyautogui.hotkey("alt", "f4")  # Close window
        response = "Closing the application."

    elif "copy" in command:
        pyautogui.hotkey("ctrl", "c")  # Copy
        response = "Copied text."

    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")  # Paste
        response = "Pasted text."

    # **Start Windows Speech-to-Text**
    elif "start dictation" in command:
        start_windows_dictation()
        response = "Dictation started. Speak now."

    # **Fetch News**
    elif "get news" in command or "latest news" in command:
        news_headlines = fetch_news()
        response = "Here are the latest news headlines:\n" + "\n".join(news_headlines)

    # Default response if command is not recognized
    if not response:
        response = "Sorry, I didn't understand that."

    # Speak the response
    speak(response)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

