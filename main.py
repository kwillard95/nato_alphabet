import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What word would you like to convert? ")
formatted_word = user_input.upper()
coded_content = [nato_alphabet_dict[letter] for letter in formatted_word]
display = [print(coded_word) for coded_word in coded_content]

