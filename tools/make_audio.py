"""Generate the game's voice clips with Azure neural text-to-speech.

Run from the repo root:  python3 tools/make_audio.py
Set AZURE_SPEECH_KEY if your network doesn't add the key for you.
The clip list matches WORDS and PARAGRAPH in index.html (w00 = first word).
"""
import os
import urllib.request

REGION = "eastus"
VOICE = "es-MX-JorgeNeural"

CLIPS = {
    "w00": "el mercado",
    "w01": "la mañana",
    "w02": "comprar",
    "w03": "la fruta",
    "w04": "el plátano",
    "w05": "barato",
    "w06": "el dinero",
    "w07": "la bolsa",
    "para": (
        "Cada sábado por la mañana voy al mercado con mi abuela. "
        "Ella siempre quiere comprar fruta fresca, como plátanos y mangos. "
        "Todo es barato, pero nunca llevamos mucho dinero. "
        "Al final, ¡mi bolsa pesa más que yo!"
    ),
    # the three cheers between screens, read with a cheerful style
    "magnifico": "¡Magnífico!",
    "guau": "¡Guau!",
    "bravo": "¡Bravo!",
}
CHEERS = {"magnifico", "guau", "bravo"}


def ssml(key, text):
    if key in CHEERS:
        body = f'<mstts:express-as style="cheerful" styledegree="2">{text}</mstts:express-as>'
    elif key == "para":
        body = f'<prosody rate="-12%">{text}</prosody>'
    else:
        body = f'<prosody rate="-8%">{text}</prosody>'
    return (
        '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
        'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="es-MX">'
        f'<voice name="{VOICE}">{body}</voice></speak>'
    )


def main():
    url = f"https://{REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
        "User-Agent": "root-rain-espanol",
    }
    if os.environ.get("AZURE_SPEECH_KEY"):
        headers["Ocp-Apim-Subscription-Key"] = os.environ["AZURE_SPEECH_KEY"]
    os.makedirs("audio", exist_ok=True)
    for key, text in CLIPS.items():
        req = urllib.request.Request(url, data=ssml(key, text).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req) as r:
            data = r.read()
        with open(f"audio/{key}.mp3", "wb") as f:
            f.write(data)
        print(f"audio/{key}.mp3  {len(data):>7} bytes  {text[:40]}")


if __name__ == "__main__":
    main()
