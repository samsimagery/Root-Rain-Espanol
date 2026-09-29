# Root Rain Español

A Spanish version of the Root Rain typing game, built as a one-off test round (not scheduled, no daily updates).

Play it: https://claude.ai/artifact/XRasiCGNX9i6y4o8dG8Myy

## How it plays

1. **Words.** All eight vocabulary words sit on the board at once. Type a word and it bursts off the screen. The clock starts on your first key and stops when the board is empty.
2. **Paragraph.** Type a four-sentence paragraph that uses the words. Punctuation fills in by itself, capitals don't matter, and accents are optional (`n` works for ñ).
3. **Your sentences.** Write your own sentences. Each of the eight words you use scores 5 points (up to 40), and other forms count too (frutas, compramos, barata).

A cheer (¡Magnífico!, ¡Guau!, ¡Bravo!) sweeps across the screen between screens. At the end, **Copy results** copies your two times and your sentence points.

Tile colours show grammar: blue for *el* words, rose for *la* words, gold for verbs and adjectives.

## Files

- `index.html`: the whole game. The word list and paragraph are the `WORDS` and `PARAGRAPH` constants near the top of the script.
- `audio/`: voice clips from Azure neural text-to-speech (Jorge, es-MX). There is no recording mode.
- `tools/make_audio.py`: regenerates the clips. If you change the words or paragraph, update its `CLIPS` list to match and run `python3 tools/make_audio.py`.

`index.html` is written for the Claude artifact host, which adds the `<!doctype html>` wrapper when it publishes. If you host it somewhere else, add a doctype and `<meta charset="utf-8">` at the top.
