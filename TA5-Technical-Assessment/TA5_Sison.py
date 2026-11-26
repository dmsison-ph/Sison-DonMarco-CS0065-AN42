from textblob import TextBlob

def main():
    counts = {"Positive": 0, "Neutral": 0, "Negative": 0}

    print("==========================================")
    print("Sentiment Analysis Summarizer by Don Sison")
    print("==========================================")

    for number in range(1, 11):
        sentence = input(f"\nEnter sentence {number}: ")
        polarity, label = analyze_sentence(sentence)
        counts[label] += 1
        print(f"Polarity: {polarity:.2f}")
        print(f"Sentiment: {label}")
    print_summary(counts)

def analyze_sentence(sentence):
    polarity = TextBlob(sentence).sentiment.polarity

    if polarity < 0:
        label = "Negative"
    elif polarity == 0:
        label = "Neutral"
    else:
        label = "Positive"

    return polarity, label

def print_summary(counts):
    print()
    print("==========================================")
    print("          Results of the analysis")
    print("==========================================")
    print(f"Your positive sentence count is {counts['Positive']}")
    print(f"Your neutral sentence count is {counts['Neutral']}")
    print(f"Your negative sentence count is {counts['Negative']}")
    print(f"Total sentences: {sum(counts.values())}")
    print("==========================================")

main()
