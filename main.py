# ------------- Made By Chinmay Bhatt -------------

import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n Jarvis: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
            {"role": "user", "content": query}
        ]
    )
    reply = response["choices"][0]["message"]["content"]
    say(reply)
    chatStr += f"{reply}\n"
    return reply

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error recognizing voice: ", e)
            return None  # Return None if nothing is recognized

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        query = takeCommand()

        # If no voice input, continue listening
        if query is None:
            continue

        # Check if user said "Jarvis"
        if "jarvis" in query.lower():
            say("Yes sir")
            continue

        # Open common websites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["instagram", "https://www.instagram.com/chinmaybhattt"],
            ["linkedin", "https://www.linkedin.com/chinmaybhattt"],
            ["twitter", "https://www.x.com/chinmaybhattt"],
            ["github", "https://github.com/chinmaybhattt"],
            ["chatgpt", "https://chatgpt.com"]
        ]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                break

        # Play music
        if "open music" in query.lower():
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"  # Replace with your music file path
            os.system(f"open {musicPath}")

        # Tell time
        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes")

        # Open specific apps
        elif "open facetime" in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass" in query.lower():
            os.system(f"open /Applications/Passky.app")

        # AI-based response
        elif "using artificial intelligence" in query.lower():
            chat(query)

        # Quit command
        elif "jarvis quit" in query.lower():
            say("Goodbye sir")
            exit()

        # Reset chat
        elif "reset chat" in query.lower():
            chatStr = ""
            say("Chat has been reset sir")

        # Default case: chat response
        else:
            chat(query)
