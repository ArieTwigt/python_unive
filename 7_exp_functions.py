#%%
from our_functions.name_functions import remove_vowels

#%%

namen_lijst = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

nieuwe_lijst, aantal_namen = remove_vowels(namen_lijst)

print(nieuwe_lijst)
# %%
from our_functions.calc_functions import calculate_pythagoras


#%%
c1, c2 = calculate_pythagoras(4, 7, return_sqrd=True)

# %% applying default parameters
calculate_pythagoras(4, 7, multiplier=2)
# %%

# %%
