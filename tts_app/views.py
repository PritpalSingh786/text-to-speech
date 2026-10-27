import asyncio
import edge_tts
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

VOICES = [
    {"id": "en-GB-RyanNeural", "name": "English (UK) - Ryan (Male, Deep & Calm)"},
    {"id": "en-US-EmmaMultilingualNeural", "name": "English (US) - Emma (Female, Soft)"},
    {"id": "en-US-AndrewNeural", "name": "English (US) - Andrew (Male, Warm)"},
    {"id": "en-IN-NeerjaNeural", "name": "English (India) - Neerja (Female)"},
    {"id": "en-US-AriaNeural", "name": "English (US) - Aria (Female, Expressive)"},
    {"id": "hi-IN-SwaraNeural", "name": "Hindi - Swara (Female)"},
    {"id": "hi-IN-MadhurNeural", "name": "Hindi - Madhur (Male)"},
]

DEMO_TEXT = "Take a deep breath... And gently close your eyes... You have done enough for today... Now, it's time to let go."

DEFAULT_VOICE = "en-GB-RyanNeural"
DEFAULT_SPEED = "0.8"

# Max Limit set to 10,000
MAX_CHARACTERS = 10000


def index(request):
    return render(request, 'tts_app/index.html', {
        'voices': VOICES,
        'default_speed': DEFAULT_SPEED,
        'default_voice': DEFAULT_VOICE,
        'max_chars': MAX_CHARACTERS,
    })


async def _generate_audio(text, voice, speed_multiplier):
    text = re.sub(r'\[Pause for \d+ seconds\]', '... ... ...', text)
    speed_val = float(speed_multiplier)
    percentage_change = int((speed_val - 1.0) * 100)
    rate_str = f"{'+' if percentage_change >= 0 else ''}{percentage_change}%"

    communicate = edge_tts.Communicate(text, voice, rate=rate_str)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data


def demo_tts(request):
    voice = request.GET.get('voice', DEFAULT_VOICE)
    speed = request.GET.get('speed', DEFAULT_SPEED)

    try:
        audio = asyncio.run(_generate_audio(DEMO_TEXT, voice, speed))
        response = HttpResponse(audio, content_type="audio/mpeg")
        response['Content-Disposition'] = 'inline; filename="demo.mp3"'
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def convert_tts(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    text = request.POST.get('text', '').strip()
    voice = request.POST.get('voice', DEFAULT_VOICE)
    speed = request.POST.get('speed', DEFAULT_SPEED)

    if not text:
        return JsonResponse({'error': 'Text cannot be empty'}, status=400)

    # Backend Limit Check (10,000 chars)
    if len(text) > MAX_CHARACTERS:
        return JsonResponse({'error': f'Text is too long. Maximum {MAX_CHARACTERS} characters allowed per conversion.'}, status=400)

    try:
        audio = asyncio.run(_generate_audio(text, voice, speed))
        response = HttpResponse(audio, content_type="audio/mpeg")
        response['Content-Disposition'] = 'attachment; filename="audio_output.mp3"'
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)