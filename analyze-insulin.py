import re

sentence = "Hello, world! This is a test sentence with some special characters: @#$%^. I want to remove 'world' and all special characters."

# Define the words and special characters to remove
words_to_remove = ['world']
special_chars_to_remove = r'[@#$%^.]'

# Use regex to remove the words and special characters from the sentence
clean_sentence = re.sub('|'.join(words_to_remove), '', sentence)
clean_sentence = re.sub(special_chars_to_remove, '', clean_sentence)

print(clean_sentence)