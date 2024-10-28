from collections import Counter

filename = 'sample.txt'

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

#This is to test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# this is to count lines
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())


num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

#this is to check the most common word
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# this is to check the avg_length
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")


def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')


# Exercise 1: Count Unique Words
def count_unique_words(content):
    # Convert all words to lowercase to ensure case-insensitivity
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

# Exercise 2: Find the Longest Word
def longest_word(content):
    words = content.split()
    longest = max(words, key=len)
    return longest

# Exercise 3: Count Occurrences of a Specific Word
def count_specific_word(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())

# Exercise 4: Calculate Percentage of Words Longer Than Average Length
def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words_count = sum(1 for word in words if len(word) > avg_length)
    return (longer_words_count / len(words)) * 100

# Main function to run all exercises and display results
def analyze_text1(filename):
    content = read_file(filename)
    unique_words = count_unique_words(content)
    # Find the longest word
    longest = longest_word(content)
    specific_word_count = count_specific_word(content, 'the')
    percent_longer_than_avg = percentage_longer_than_average(content)

    # Display the results
    print('\n')
    print('Lab Exercise Answers:')
    print(f"Number of unique words: {unique_words}")
    print(f"Longest word: '{longest}'")
    print(f"Occurrences of the word 'the': {specific_word_count}")
    print(f"Percentage of words longer than average length: {percent_longer_than_avg:.2f}%")

# Run the analysis with a sample text file
analyze_text1('sample1.txt')
