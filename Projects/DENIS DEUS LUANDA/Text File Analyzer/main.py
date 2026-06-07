from collections import Counter
import string
import os

# Get the folder where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the text file
filename = os.path.join(script_dir, "PythonSavvy.txt")

with open(filename, "r") as file:
    content = file.read().lower()

# Count characters in the original text
character_count = len(content)

# Count lines in the original text
line_count = len(content.splitlines())

# Split text into words
words = content.split()

# Remove punctuation from each word
words = [word.strip(string.punctuation) for word in words]

# Remove any empty strings that may result from punctuation-only words
words = [word for word in words if word]

# Count words after cleaning
word_count = len(words)

# Count word frequencies
frequency = Counter(words)

# Get the top 5 most common words
top_words = frequency.most_common(5)

# Display file statistics
print("=" * 40)
print("TEXT FILE ANALYSIS")
print("=" * 40)

print(f"Number of Characters: {character_count}")
print(f"Number of Lines     : {line_count}")
print(f"Number of Words     : {word_count}")

# Display word frequencies
print("\nWORD FREQUENCIES")
print("-" * 40)

for word, count in frequency.items():
    print(f"{word:<15} : {count}")

# Display top 5 most common words
print("\nTOP 5 MOST COMMON WORDS")
print("-" * 40)

for word, count in top_words:
    print(f"{word:<15} : {count}")