student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}




    # phonetic_dictionary = {letter:code for (letter, code) in data}
    # print(phonetic_dictionary)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
keep_going = True
while keep_going:
    answer = input("Enter a word or letter: ").upper()
    try:
        listword = [phonetic_dictionary[letter] for letter in answer]
    except KeyError:
        print("Sorry, please enter only alphabetical characters, no numbers")
    else:
        print(listword)
