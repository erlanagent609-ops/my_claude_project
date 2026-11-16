import sys
import re
from collections import Counter

def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Word count
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)

    # Sentence count (simple heuristic using punctuation)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Word frequency
    word_freq = Counter(words)

    print(f"--- Text Analysis Results for {file_path} ---")
    print(f"Total Words: {word_count}")
    print(f"Total Sentences: {sentence_count}")
    print("\nTop 5 Most Frequent Words:")
    for word, freq in word_freq.most_common(5):
        print(f"  {word}: {freq}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_text(sys.argv[1])
    else:
        print("Usage: python scripts/text_analyzer.py <path_to_text_file>")
