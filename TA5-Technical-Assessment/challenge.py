import re
import nltk
from nltk.corpus import opinion_lexicon

try:
    happy_words = set(opinion_lexicon.positive())
    sad_words = set(opinion_lexicon.negative())
except LookupError:
    print("Downloading the Opinion Lexicon dataset...")
    nltk.download("opinion_lexicon")
    happy_words = set(opinion_lexicon.positive())
    sad_words = set(opinion_lexicon.negative())


def get_words(sentence):
    """Convert a sentence into lowercase words without punctuation."""
    return re.findall(r"[a-zA-Z]+(?:[-'][a-zA-Z]+)*", sentence.lower())


def number_happy(sentence):
    """Return the number of happy words in the sentence."""
    words = get_words(sentence)
    return sum(1 for word in words if word in happy_words)


def number_sad(sentence):
    """Return the number of sad words in the sentence."""
    words = get_words(sentence)
    return sum(1 for word in words if word in sad_words)


print("========================================")
print("     HAPPINESS AND SADNESS ANALYZER")
print("========================================")

sentence = input("Enter a sentence: ")

happy_count = number_happy(sentence)
sad_count = number_sad(sentence)

print("\n========================================")
print("             ANALYSIS RESULT")
print("========================================")
print(f"Number of happy words: {happy_count}")
print(f"Number of sad words:   {sad_count}")

if happy_count > sad_count:
    print("Analysis: Positive")
    print("Tone: Happy")
elif sad_count > happy_count:
    print("Analysis: Negative")
    print("Tone: Sad")
else:
    print("Analysis: Neutral")
    print("Tone: Neutral")

print("========================================")