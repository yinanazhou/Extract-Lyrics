import os
import json
import matplotlib.pyplot as plt
from collections import Counter
import argparse

if __name__ == "__main__":
    trg_path = "moody_lyrics.json"
    with open(trg_path) as f:
        song_info = json.load(f)

    print("Artist: " + song_info["Artist"][0][100])
    print("Title: " + song_info["Title"][0][100])
    print("Lyric: " + song_info["Lyric"][0][100])
    print("Mood: " + song_info["Mood"][0][100])
