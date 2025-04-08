import re
from collections import Counter

def get_word_counts(file_path):
    """Extracts words and counts their occurrences in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase
    
    words = re.findall(r'\b\w+\b', text)  # Extract words ignoring punctuation
    return Counter(words)  # Returns a dictionary with word counts

def find_common_words(file1, file2):
    word_counts_file1 = get_word_counts(file1)
    word_counts_file2 = get_word_counts(file2)

    common_words = set(word_counts_file1.keys()) & set(word_counts_file2.keys())  # Words in both files

    print("\nTotal number of common words:", len(common_words))

    if common_words:
        print("\nWords present in both files with their counts:")
        for word in common_words:
            print(f"{word}: File 1 ({word_counts_file1[word]}), File 2 ({word_counts_file2[word]})")
    else:
        print("\nNo common words found between the two files.")

    print("\nWord Counts in Each File:")
    print(f"File 1 ({file1}): {sum(word_counts_file1.values())} words")
    print(f"File 2 ({file2}): {sum(word_counts_file2.values())} words")

# Example Usage:
file1 = "excel.txt"  # Replace with actual file name
file2 = "hasss.txt"  # Replace with actual file name
find_common_words(file1, file2)
