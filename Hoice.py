import tkinter as tk
from tkinter import Label, Button
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import pyjokes
import requests
import random
import smtplib

# ============================================================
#  CONFIGURATION — Fill these in before running
# ============================================================
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"   # https://openweathermap.org/api
NEWS_API_KEY    = "YOUR_NEWSAPI_KEY"               # https://newsapi.org
EMAIL_ADDRESS   = "your_gmail@gmail.com"           # Your Gmail address
EMAIL_PASSWORD  = "your_app_password"              # Gmail App Password (not your Gmail password)
                                                   # Generate at: https://myaccount.google.com/apppasswords
# ============================================================

# === Text to Speech Setup ===
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    response_label.config(text=f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()

# === Email ===
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, content)
        server.close()
    except Exception as e:
        speak("Sorry, I was unable to send the email.")
        print(f"Email error: {e}")

# === Greeting ===
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Here I am to help you.")

# === Take Voice Command ===
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        query_label.config(text="Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query_label.config(text="Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query_label.config(text=f"You said: {query}")
    except Exception as e:
        query_label.config(text="Say that again please...")
        return "None"
    return query

# === Joke, Quote, Fact ===
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def tell_quote():
    quotes = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Hard work beats talent when talent doesn't work hard.",
        "Push yourself, because no one else is going to do it for you.",
        "The only way to do great work is to love what you do.",
        "Believe you can and you're halfway there."
    ]
    speak(random.choice(quotes))

def tell_fact():
    facts = [
        "Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts and blue blood.",
        "A group of flamingos is called a flamboyance.",
        "The Eiffel Tower can grow about 6 inches taller in summer due to heat expansion."
    ]
    speak(random.choice(facts))

# === Weather (OpenWeatherMap API) ===
def get_weather(query):
    if "weather in" in query:
        city = query.split("weather in")[-1].strip()
    else:
        speak("Please say the city name. For example: weather in Delhi.")
        return

    if WEATHER_API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        speak("Weather API key is not set. Please add your OpenWeatherMap API key in the configuration section.")
        return

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(complete_url).json()
        if response.get("cod") == 200:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            speak(f"The temperature in {city.capitalize()} is {temp} degrees Celsius with {desc}.")
        else:
            message = response.get("message", "something went wrong")
            speak(f"Sorry, I couldn't find the weather for {city}. Reason: {message}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather right now.")
        print(f"Weather error: {e}")

# === News (NewsAPI) ===
def get_news():
    if NEWS_API_KEY == "YOUR_NEWSAPI_KEY":
        speak("News API key is not set. Please add your NewsAPI key in the configuration section.")
        return

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url).json()
        if response.get("status") == "ok" and response.get("articles"):
            speak("Here are today's top news headlines:")
            for i, article in enumerate(response["articles"][:5], 1):
                title = article.get("title")
                if title:
                    speak(f"News {i}: {title}")
        else:
            speak("Sorry, I couldn't fetch the news right now.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the news right now.")
        print(f"News error: {e}")

# === Play Music ===
def play_music():
    # Change this path to your music folder
    music_dir = os.path.join(os.path.expanduser("~"), "Music")
    if os.path.exists(music_dir):
        songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        if songs:
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak("Playing music.")
        else:
            speak("No music files found in your Music folder.")
    else:
        speak("Music folder not found. Please update the music directory path in the code.")

# === Core Command Handler ===
def run_assistant():
    wishMe()
    query = takeCommand().lower()

    if query == "none":
        return

    if 'news' in query:
        get_news()

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "").strip()
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(results)
        except Exception as e:
            speak("Sorry, I couldn't find that on Wikipedia.")

    elif 'youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif 'google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif 'play music' in query:
        play_music()

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {strTime}.")

    elif 'joke' in query:
        tell_joke()

    elif 'quote' in query:
        tell_quote()

    elif 'fact' in query:
        tell_fact()

    elif 'weather in' in query:
        get_weather(query)

    elif 'email' in query:
        try:
            speak("Who should I send the email to? Please say the email address.")
            to = takeCommand()
            speak("What should I say?")
            content = takeCommand()
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            speak("Sorry, I was unable to send the email.")
            print(f"Email error: {e}")

    else:
        speak("I didn't understand that. Please try again.")

# === GUI Setup ===
root = tk.Tk()
root.title("Voice Assistant - Herab")
root.geometry("500x300")
root.resizable(False, False)

title_label = Label(root, text="AI POWERED BY HERAB", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

query_label = Label(root, text="Press the button and speak...", font=("Helvetica", 12))
query_label.pack(pady=20)

response_label = Label(root, text="", font=("Helvetica", 12), fg="blue", wraplength=400)
response_label.pack(pady=10)

start_button = Button(root, text="Speak", font=("Helvetica", 14), bg="orange", fg="yellow", command=run_assistant)
start_button.pack(pady=20)

root.mainloop()
