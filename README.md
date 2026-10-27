# 🎙️ AI Voice Converter — Text to Speech

A free Text-to-Speech (TTS) web application built with **Python, Django, and Edge-TTS**. Convert text into natural-sounding speech with customizable voice and speed settings, listen to the generated audio, and download it as an MP3 file.

🎥 **[Watch the Demo on YouTube](https://youtu.be/QwmklFhqt2E)**

## ✨ Features

- **Free TTS Engine:** Uses the `edge-tts` Python package.
- **Long Text Support:** Supports up to 10,000 characters per conversion.
- **Adjustable Speech Speed:** Customize speed from 0.1x to 2.0x.
- **Multiple Voices:** Supports selected English and Hindi voices, including US, UK, and Indian options.
- **Audio Preview:** Listen to a sample before generating the full audio.
- **Progress Tracking:** Track the conversion process.
- **MP3 Download:** Play generated speech in the browser or download the audio.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Text-to-Speech:** Edge-TTS
- **Frontend:** HTML5, CSS3, JavaScript

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version
- pip
- Internet connection for Edge-TTS

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

**3. Install dependencies**

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install django edge-tts
```

**4. Apply database migrations**

```bash
python manage.py migrate
```

**5. Start the development server**

```bash
python manage.py runserver
```

**6. Open the application**

Visit http://127.0.0.1:8000/ in your browser.

## 📂 Project Structure

```text
tts_project/
├── tts_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tts_app/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── tts_app/
│           └── index.html
├── manage.py
└── requirements.txt
```

*Note: The structure above is an example. Update it to match your actual project files.*

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

Add your preferred open-source license to the repository. If you choose the MIT License, include the license text in a `LICENSE` file.

## ⚠️ Disclaimer

This project uses Edge-TTS, which relies on Microsoft's online text-to-speech service. It requires an internet connection and is not an offline TTS solution. Service availability and usage are subject to the provider's terms and policies.
