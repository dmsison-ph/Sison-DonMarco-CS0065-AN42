import re

import nltk
from nltk.corpus import opinion_lexicon

try:
    happy_words = set(opinion_lexicon.positive())
    sad_words = set(opinion_lexicon.negative())
except LookupError:
    print("Downloading the Opinion Lexicon dataset...")
    if not nltk.download("opinion_lexicon"):
        raise RuntimeError("Could not download the Opinion Lexicon dataset.")

    happy_words = set(opinion_lexicon.positive())
    sad_words = set(opinion_lexicon.negative())

def main():
    print("===========================================")
    print("Happiness and Sadness Analyzer by Don Sison")
    print("===========================================")

    for number in range(1, 4):
        print()
        sentence = input(f"Enter sentence {number} of 3: ")

        happy_count = number_happy(sentence)
        sad_count = number_sad(sentence)

        print()
        print(f"========== Sentence {number} Result ==========")
        print(f"Happy words: {happy_count}")
        print(f"Sad words:   {sad_count}")

        if happy_count > sad_count:
            print("Analysis: Positive")
            print("Tone: Happy")
        elif sad_count > happy_count:
            print("Analysis: Negative")
            print("Tone: Sad")
        else:
            print("Analysis: Neutral")
            print("Tone: Neutral")

    print()
    print("===========================================")
    print("       All 3 sentences analyzed")
    print("===========================================")

def get_words(sentence):
    return re.findall(r"[a-zA-Z]+(?:[-'][a-zA-Z]+)*", sentence.lower())

def number_happy(sentence):
    return sum(1 for word in get_words(sentence) if word in happy_words)

def number_sad(sentence):
    return sum(1 for word in get_words(sentence) if word in sad_words)

main()