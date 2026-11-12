from textblob import TextBlob


positive_count = 0
neutral_count = 0
negative_count = 0


print("========================================")
print("       SENTIMENT ANALYSIS PROGRAM")
print("========================================")

for number in range(1, 11):
    sentence = input(f"\nEnter sentence {number}: ")

    sentiment = TextBlob(sentence)
    polarity = sentiment.sentiment.polarity

    print(f"Polarity: {polarity:.2f}")

    if polarity < 0:
        print("Sentiment: Negative")
        negative_count += 1

    elif polarity == 0:
        print("Sentiment: Neutral")
        neutral_count += 1

    else:
        print("Sentiment: Positive")
        positive_count += 1


print("\n========================================")
print("        SENTIMENT ANALYSIS SUMMARY")
print("========================================")
print(f"Positive sentences: {positive_count}")
print(f"Neutral sentences:  {neutral_count}")
print(f"Negative sentences: {negative_count}")
print(f"Total sentences:    {positive_count + neutral_count + negative_count}")
print("========================================")
