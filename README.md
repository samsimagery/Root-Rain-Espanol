# Las frases del día

A Spanish typing game based on Root Rain, built as a one-off test round (not scheduled, no daily updates).

Play it: https://claude.ai/artifact/XRasiCGNX9i6y4o8dG8Myy

## How it plays

1. **Phrases.** Three famous phrases from Spanish literature sit highlighted inside their real passages on the board:
   - *de cuyo nombre no quiero acordarme* (Cervantes, *Don Quijote*)
   - *se hace camino al andar* (Antonio Machado, *Campos de Castilla*)
   - *la vida es sueño* (Calderón de la Barca, *La vida es sueño*)

   Type a phrase, spaces included, and its letters light up as you go. When it's complete it bursts out of the text and off the screen. The clock starts on your first key and stops when all three are gone. Accents are optional (`n` works for ñ) and capitals don't matter.
2. **Examples.** Each phrase in its original passage and in two everyday sentences, with a button to hear each one. Nothing to type here.
3. **Your sentence.** Write one creative sentence that uses one of the three phrases word for word, plus at least two words of your own. The Finish button unlocks once it does.

A cheer (¡Magnífico!, ¡Guau!, ¡Bravo!) sweeps across the screen between screens. The last screen shows your sentence, and **Copy results** copies it together with your time and the link to play.

## Files

- `index.html`: the whole game. The phrases, passages and examples are the `PHRASES` constant near the top of the script.
- `audio/`: voice clips from Azure neural text-to-speech (Jorge, es-MX). There is no recording mode.
- `tools/make_audio.py`: regenerates the clips. If you change the phrases, passages or examples, update its `CLIPS` list to match and run `python3 tools/make_audio.py`.

`index.html` is written for the Claude artifact host, which adds the `<!doctype html>` wrapper when it publishes. If you host it somewhere else, add a doctype and `<meta charset="utf-8">` at the top.
