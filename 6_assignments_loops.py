## Assignments

#%%
# 1.
namen_lijst = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

namen_lijst_filtered = []

# remove vowels from names in list
for naam in namen_lijst:
    print(naam)
    for letter in naam:
        if letter in vowels:
            naam = naam.replace(letter, '')
    print(naam)
    print("\n")
    namen_lijst_filtered.append(naam)

#%%
print(namen_lijst_filtered)


#%%
# 2.
from datetime import datetime, timedelta

# create variable with current date
date_today = datetime.today()

# define data range
day_range = range(1, 11)


#%% a. 
for day in day_range:
    new_date = date_today + timedelta(days=day)
    print(new_date.strftime("%A"))
        

# %% b.
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')

for day in day_range:
    new_date = date_today + timedelta(days=day)
    print(new_date.strftime(f"Over {day} dagen is het :%A in het jaar %Y"))

# %% c.
i = 1
max_days = 10

while i <= max_days:
    new_date = date_today + timedelta(days=i)
    print(new_date.strftime("%A"))
    i += 1
# %%
