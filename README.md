# Weather App (Python + Flask + Requests)

A colorful browser-based Weather App built with Python and Flask. It fetches real-time weather from OpenWeatherMap using the `requests` library and shows it in a modern web UI. Includes demo mode (no API key needed) and robust error handling.

---

## ✨ Features
- GUI with Tkinter (city input + Get Weather button + results panel)
- Real-time weather: temperature (°C), feels-like, humidity, condition
- Error handling: invalid city, invalid API key, network errors, timeouts
- Demo mode when API key is missing (shows sample data)
- Clean, readable code with comments

---

## 📦 Requirements
- Python 3.8+
- `Flask` + `requests` (installed via `requirements.txt`)

---

## 🛠️ Setup (Windows PowerShell)

```powershell
# 1) Go to your workspace folder
cd C:\Users\<YOU>\Desktop\weather\weather-app

# 2) (If not created already) create & activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt
```

Mac/Linux equivalents:
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

---

## 🔑 Get OpenWeatherMap API Key
1. Visit: https://openweathermap.org/
2. Sign Up → Verify email → Log in
3. Go to Profile → API keys → Copy your key

---

## ⚙️ Configure API Key (Real Data)
Open `weather_service.py` and set your API key:

```python
api_key = "YOUR_REAL_API_KEY"
```

Save the file and run the app.

---

## 🧪 Demo Mode (No API Key Needed)
If `api_key` is left as `"YOUR_API_KEY"` or the placeholder value in `weather_service.py`, the app automatically shows demo weather data instead of failing. This lets you test the UI without a key.

---

## ▶️ Run the App (Browser)
From inside the `weather-app` folder:

PowerShell:
```powershell
cd C:\Users\<YOU>\Desktop\weather\weather-app
.\venv\Scripts\activate
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000/
```

---

## 🧰 Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Invalid API Key | Placeholder key or wrong key | Replace with your real key in `weather_app.py` |
| City not found | Misspelling/unsupported city | Try another spelling or a major city |
| requests not installed | Missing dependency | `pip install requests` inside the venv |
| 401 Unauthorized | Key not active/incorrect | Wait a few minutes after signup; verify the key |
| Connection/Timeout | Network issues | Check your internet and retry |

---

## 📁 Project Structure
```
weather-app/
├─ venv/                  # Virtual environment (local)
├─ app.py                 # Flask web app (entry point)
├─ weather_service.py     # Weather fetching + demo mode logic
├─ requirements.txt       # Dependencies
├─ templates/
│  └─ index.html          # HTML template for UI
└─ static/
   └─ styles.css          # Colorful CSS styling
```

---

## 🧠 How It Works
- Flask serves a web page (`index.html`) with a city input and "Get Weather" button.
- On submit, the server uses `WeatherService` (in `weather_service.py`) to call OpenWeatherMap.
- `requests.get()` fetches JSON; values are extracted and rendered into the template.
- Errors are caught and shown as a red banner in the UI.
- If the API key is missing, demo weather data is returned instead of failing.

---

## 🌍 API Endpoint Used
```
http://api.openweathermap.org/data/2.5/weather?q=<CITY>&appid=<API_KEY>&units=metric
```

---

## 📜 License
This project is for learning/demo purposes. You may modify and use it freely.

---

## 🇬🇧 English + 🇮🇳 తెలుగు (Telugu)

### What this app does / ఈ app ఏమి చేస్తుంది
- **English**: Shows real-time weather (temperature, humidity, condition) for any city using OpenWeatherMap API.
- **Telugu**: ఈ app OpenWeatherMap API ఉపయోగించి ఏ city కి అయినా real-time weather (temperature, humidity, condition) చూపిస్తుంది.

### Setup steps / సెటప్ స్టెప్స్
- **English**:
  1) Create venv → activate → `pip install requests`
  2) Put your API key in `weather_app.py`
  3) Run `python weather_app.py`
- **Telugu**:
  1) venv create చేసి activate చేయండి → `pip install requests`
  2) మీ API key ని `weather_app.py` లో పెట్టండి
  3) `python weather_app.py` run చేయండి

### Demo mode / డెమో మోడ్
- **English**: No key? The app shows sample weather so you can test UI.
- **Telugu**: API key లేకపోయినా, app demo data చూపిస్తుంది, UI ని test చేయవచ్చు.

### Common errors / సాధారణ errors
- **Invalid API Key** → Put correct key and wait few minutes after signup.
- **City not found** → City spelling check చేయండి.
- **requests not installed** → `pip install requests`.

---

## 💼 Resume Snippet
- Built a Python web-based Weather App using Flask and `requests`, integrating OpenWeatherMap’s REST API. Implemented robust error handling, demo mode (no key required), and a modern, colorful browser UI. Demonstrated skills in web development, HTTP/JSON processing, and dependency management with virtual environments.

**Telugu**: Flask మరియు `requests` ఉపయోగించి Python లో web-based Weather App తయారు చేసాను. OpenWeatherMap REST API integrate చేసి, error handling, demo mode (API key లేకపోయినా), modern colorful browser UI implement చేసాను. Web development, HTTP/JSON processing, virtual environments లో dependency management లో నైపుణ్యం చూపించాను.



