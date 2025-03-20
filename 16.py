from collections import Counter
import re

def most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lowercase
    word_counts = Counter(words)  # Count occurrences of each word
    most_common = word_counts.most_common(1)  # Get the most common word
    return most_common[0] if most_common else None  # Return the most common word and its count

# Example usage
text = "This is a sample text. This text is simple and simple. bla bla bla  bla bla"
print(most_common_word(text))
