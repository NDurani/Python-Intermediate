import pandas


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

file = pandas.read_csv('nato_phonetic_alphabet.csv')

# w_dict = {index[1].letter: index[1].code for index in file.iterrows()}
w_dict = {row.letter: row.code for index, row in file.iterrows()}

print(w_dict)