"""Generate the game's voice clips with Azure neural text-to-speech.

Run from the repo root:  python3 tools/make_audio.py
Set AZURE_SPEECH_KEY if your network doesn't add the key for you.
The clip list matches PHRASES in index.html (p0 = first phrase, o0 its passage, e0a/e0b its examples).
"""
import os
import urllib.request

REGION = "eastus"
VOICE = "es-MX-JorgeNeural"

CLIPS = {
    # the three phrases
    "p0": "de cuyo nombre no quiero acordarme",
    "p1": "se hace camino al andar",
    "p2": "la vida es sueño",
    # the passages they come from, as shown on the board
    "o0": (
        "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, "
        "no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero…"
    ),
    "o1": (
        "Caminante, son tus huellas el camino y nada más; "
        "caminante, no hay camino, se hace camino al andar."
    ),
    "o2": (
        "¿Qué es la vida? Una ilusión, una sombra, una ficción, "
        "y el mayor bien es pequeño; que toda la vida es sueño, "
        "y los sueños, sueños son."
    ),
    # everyday examples
    "e0a": "Trabajé en una oficina de cuyo nombre no quiero acordarme.",
    "e0b": "Anoche cenamos en un restaurante de cuyo nombre no quiero acordarme.",
    "e1a": "No tengo un plan perfecto, pero se hace camino al andar.",
    "e1b": "Aprender español es difícil, pero se hace camino al andar.",
    "e2a": "Mi abuela siempre dice que la vida es sueño.",
    "e2b": "Cuando miro las estrellas, siento que la vida es sueño.",
    # the three cheers between screens, read with a cheerful style
    "magnifico": "¡Magnífico!",
    "guau": "¡Guau!",
    "bravo": "¡Bravo!",
}
CHEERS = {"magnifico", "guau", "bravo"}


def ssml(key, text):
    if key in CHEERS:
        body = f'<mstts:express-as style="cheerful" styledegree="2">{text}</mstts:express-as>'
    elif key.startswith("o"):
        body = f'<prosody rate="-15%">{text}</prosody>'
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
