# Group_Project
# Tewana_Mellace

print('Welcome to my version of Wordle!\n')
print('INSTRUCTIONS:')
print('1. You have 6 chances to guess the 5 letter word based off the given definition.')
print('2. Green tile means the letter is in the word and in the correct spot')
print('3. Yellow tile means that the letter is in the word but in the incorrect spot')
print('4. Red tile means the letter is not in the word\n')
print('Lets Play!!!\n')


import random
dictionary = {'Aback' : 'toward or situated to the rear; back. (adverb)',
              'Abase' : 'behave in a way that belittles or degrades (verb)',
              'Abate' : 'of something perceived as hostile threatening or negative, become less intense or widespread. (verb)',
              'boost' : 'a source of help or encouragement leading to increase or improvement. (noun)',
              'favor' : 'feel or show approval or preference for. (verb)',
             }
d = dictionary
entry_list = list(d.values())

random_entry = random.choice(entry_list)
print(f"The definition is: {random_entry.upper()}\n\n")

"""
if random_entry in d.values():
    print(f"Yes, Value: '{random_entry}' exists in dictionary\n\n")
else:
    print(f"No, Value: '{random_entry}' does not exists in dictionary\n\n")
"""

def method(d, value):
    for k, random_entry in d.items():
        if random_entry == value:
            yield k


for r in method(d, random_entry):
    key = r
    print(f'NB!!!!!! This should no be visible to the user. This is the word they are trying to guess!!!!!: {key.upper()}\n\n')



users_word = input("Please make your first attempt at guessing the 5 letter word based off the definition given above ^. \nAttempt:")

count = 0
if key.upper() == users_word.upper() and count >= 5:
    print('Congratulations! You are correct!!!')
else:
    while key.upper() != users_word.upper() and count >= 5:
        count += 1


"""
if key.upper() == users_word.upper():
    print('Congratulations! You are correct!!!')
else:
    print('false')
"""

