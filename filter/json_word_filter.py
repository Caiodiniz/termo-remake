import os
import json

# Get the absolute path of the script's directory
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'words_dictionary.json')

# Try to open the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Filter keys (words) with 5 letters
five_letter_words = [word for word in data.keys() if isinstance(word, str) and len(word) == 5]

# Create a new dictionary with the filtered words
new_dictionary = {word: data[word] for word in five_letter_words}

# Save the new JSON file with a list of words
output_file_path = os.path.join(script_dir, 'five_letter_words.json')
with open(output_file_path, 'w') as new_file:
    json.dump(five_letter_words, new_file, indent=2)

print("File generated successfully!")
