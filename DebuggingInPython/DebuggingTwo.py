"""
Word Reversal
Given a string which is a sentence,
reverse each word in the sentence.
Then return the reversed words sentence.
"""

def reverse_words(sentence):
    words = sentence.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Example usage

sentence = "Hello world"
print(reverse_words(sentence))