# 🎙️ Herab's Voice Assistant — AI Powered Desktop Assistant

> A Python-based desktop voice assistant with a GUI that listens to your voice, understands your commands, and responds with speech. Powered by Google Speech Recognition, Wikipedia, live weather, live news, and more.

**Developed by: Herab Modi**

---

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [API Keys Setup](#api-keys-setup)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Voice Commands](#voice-commands)
- [Project Structure](#project-structure)

---

## 📌 About the Project

A desktop voice assistant built with Python and Tkinter. Press the **Speak** button, say a command, and the assistant responds with both voice and text. It uses Google's Speech Recognition API for understanding speech, and integrates with Wikipedia, OpenWeatherMap, and NewsAPI for real-time information.

---

## ✨ Features

- 🎤 **Voice Recognition** — Listens via microphone using Google Speech Recognition
- 🔊 **Text-to-Speech** — Responds in a natural voice using pyttsx3
- 📖 **Wikipedia Search** — Summarizes any Wikipedia topic
- 🌐 **Open Websites** — Opens YouTube, Google on voice command
- 🌤️ **Live Weather** — Real-time weather for any city (OpenWeatherMap API)
- 📰 **Live News** — Top 5 news headlines from India (NewsAPI)
- 🎵 **Play Music** — Plays a random song from your Music folder
- ⏰ **Current Time** — Tells the current time
- 😄 **Jokes** — Random jokes via pyjokes
- 💬 **Quotes** — Motivational quotes
- 🧠 **Facts** — Interesting random facts
- 📧 **Send Email** — Send emails via voice (Gmail SMTP)
- 🖥️ **GUI** — Clean Tkinter window showing live status and responses

---


## ⚙️ Requirements

### 🐍 Python
- **Python 3.8 or above**
- Download: https://www.python.org/downloads/
- ✅ Check **"Add Python to PATH"** during installation

### 💻 Operating System
- **Windows only** — uses `pyttsx3` with `sapi5` voice engine (Windows built-in)
- For Linux/macOS, the TTS engine setup is different

### 📦 Python Libraries

Install all at once:
```bash
pip install -r requirements.txt
```

| Library | Purpose |
|---------|---------|
| `pyttsx3` | Text-to-speech (offline, no API needed) |
| `SpeechRecognition` | Converts microphone audio to text via Google |
| `wikipedia` | Fetches Wikipedia summaries |
| `pyjokes` | Random programming/general jokes |
| `requests` | HTTP calls for weather and news APIs |
| `pyaudio` | Microphone input (required by SpeechRecognition) |

> ⚠️ **PyAudio install issue on Windows?** If `pip install pyaudio` fails, run this instead:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### 🔑 API Keys Required (Free)

| API | What it does | Get it here |
|-----|-------------|-------------|
| OpenWeatherMap | Live weather for any city | https://openweathermap.org/api |
| NewsAPI | Top news headlines | https://newsapi.org |

Both are **completely free** — no credit card needed.

---

## 🔑 API Keys Setup

### 1. OpenWeatherMap (Weather)
1. Go to https://openweathermap.org/api and sign up (free)
2. Go to **API Keys** section in your account
3. Copy your API key
4. Open `Hoice.py` and paste it here:
```python
WEATHER_API_KEY = "paste_your_key_here"
```

### 2. NewsAPI (News)
1. Go to https://newsapi.org and sign up (free)
2. Your API key is shown on the dashboard
3. Open `Hoice.py` and paste it here:
```python
NEWS_API_KEY = "paste_your_key_here"
```

### 3. Gmail (Email — Optional)
> ⚠️ Do NOT use your actual Gmail password. Use an **App Password** instead.

1. Enable 2-Factor Authentication on your Google account
2. Go to: https://myaccount.google.com/apppasswords
3. Generate an app password for "Mail"
4. Open `Hoice.py` and fill these:
```python
EMAIL_ADDRESS  = "your_gmail@gmail.com"
EMAIL_PASSWORD = "your_16_char_app_password"
```

---

## 🚀 Installation & Setup

### Step 1 — Clone the repository
```bash
git clone https://github.com/your-username/herab-voice-assistant.git
cd herab-voice-assistant
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

> If PyAudio fails:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### Step 3 — Add your API keys
Open `Hoice.py` and fill in the configuration section at the top:
```python
WEATHER_API_KEY = "your_openweathermap_key"
NEWS_API_KEY    = "your_newsapi_key"
EMAIL_ADDRESS   = "your_gmail@gmail.com"
EMAIL_PASSWORD  = "your_app_password"
```

### Step 4 — Run the assistant
```bash
python Hoice.py
```

---

## ▶️ How to Run

1. Run `python Hoice.py`
2. The GUI window opens
3. Click the orange **"Speak"** button
4. Wait for **"Listening..."** to appear
5. Speak your command clearly
6. The assistant responds with voice + text on screen

---

## 🎤 Voice Commands

| Say this... | What happens |
|------------|-------------|
| `"what is Python on Wikipedia"` | Summarizes Python from Wikipedia |
| `"open YouTube"` | Opens YouTube in browser |
| `"open Google"` | Opens Google in browser |
| `"what is the time"` | Tells current time |
| `"weather in Delhi"` | Gives live weather for Delhi |
| `"tell me the news"` | Reads top 5 news headlines |
| `"play music"` | Plays a random song from your Music folder |
| `"tell me a joke"` | Tells a random joke |
| `"give me a quote"` | Shares a motivational quote |
| `"tell me a fact"` | Shares an interesting fact |
| `"send an email"` | Starts email sending flow |

---

## 📁 Project Structure

```
herab-voice-assistant/
│
├── Hoice.py            # Main Python script (all logic + GUI)
├── requirements.txt    # All required Python libraries
├── screenshots/        # GUI screenshots
│   └── screenshot.png
└── README.md           # This file
```

---

## ⚠️ Important Notes

- **Windows only** in its current form (pyttsx3 uses Windows SAPI5 voice engine)
- Make sure your **microphone is connected and working** before running
- The assistant needs an **internet connection** for Wikipedia, weather, and news
- For the email feature, use a **Gmail App Password** — never put your real Gmail password in code
- Music playback looks for `.mp3` and `.wav` files in your system's default `~/Music` folder

---

## 🧑‍💻 Author

**Herab Modi**
- Personal Project — Python Voice Assistant with GUI
- Built with Python, Tkinter, pyttsx3, and SpeechRecognition
