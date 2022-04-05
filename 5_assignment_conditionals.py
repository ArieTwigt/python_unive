## Assignments

#%% Assignment 1/2
name = "Arie"


#%% a.
if "A" in name:
    print("Your name contains the letter A")

#%%
if "a" in name.lower():
    print("Your name contains the letter a")


## Assignment 2

#%% 
vowels = 'aeiou'
vowels_list = ['a', 'e', 'i', 'o', 'u']

#%% a.
if name[0].lower() in vowels:
    print("Your name starts with a vowel")
    name.replace(name[0], "B")

#%% b. 
if name[0].lower in vowels:
    print("Your name starts with a vowel")
    name.replace(name[0], "B", 1) # make sure only the first occurance will be replaced

# %% c.
import string
import random

all_letters_list = list(string.ascii_lowercase)
vowels_list = ['a', 'e', 'i', 'o', 'u']
non_vowels_list = [letter for letter in all_letters_list if letter not in vowels_list]

#%%

name = "Arie"

if name[0].lower() in vowels:
    random_letter = random.choice(non_vowels_list)
    name_new = random_letter.upper() + name[1:]
    print(name_new)

# %%
