# Bruindle

BRUINDLE is a Wordle alternative with three themed word lists: UCLA, CS 30, and LA. You get 6 guesses for each hidden word, and after every guess the game tells you which letters are in the right position, which are in the word but in the wrong position, and which are not in the word.

## Play in your browser (no install)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jinwangli2006-dev/Bruindle/blob/main/Bruindle_(UCLA_Wordle_Game).ipynb)

Open the notebook above and run the code cell.

## Play in a terminal

You need Python 3. It uses only the standard library, so there is nothing to install.

```
git clone https://github.com/jinwangli2006-dev/Bruindle.git
cd Bruindle
python bruindle.py
```

## How to play

1. Pick a version: `uc` (UCLA words), `cs` (CS 30 words), or `la` (LA words).
2. The game tells you how long the hidden word is.
3. Enter a guess of that length. After each guess you get three lists: right position, wrong position, and not in the word.
4. Guess the word within 6 tries to win.
