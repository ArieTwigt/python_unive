#%%
namen_lijst = ['arie', 'peter', 'jaap', 'gert']

# %% simpele loop
for i in namen_lijst:
    print(i.upper())
    print(i.capitalize)

# %% for loop met beschrijvende namen van variabelen
for naam in namen_lijst:
    print(naam.upper())
    print(naam.capitalize())


#%% enumerate() loop
for idx, naam in enumerate(namen_lijst):
    print(f"De naam {naam} heeft index {idx}")


# %% Namen in lijst upper casen met een normale loop
namen_lijst = ['arie', 'peter', 'jaap', 'gert']

namen_lijst_upper = []

for naam in namen_lijst:
    namen_lijst_upper.append(naam.upper())

print(namen_lijst_upper)

# %% Namen in lijst upper casen met een list comprehension
namen_lijst_upper = [naam.upper() for naam in namen_lijst]

# %%
getallen_lijst = [4, 6, 7, 1, 7, 8, 1,4, 5, 7, 8, 4, 4, 9, 9, 2, 13, 7, 8]

getallen_lijst_high = []
getallen_lijst_low = []

for getal in getallen_lijst:
    if getal > 5:
        getallen_lijst_high.append(getal)
    else:
        getallen_lijst_low.append(getal)

print(getallen_lijst_high)
print(getallen_lijst_low)

# %%
getallen_lijst_filtered = [getal for getal in getallen_lijst if getal > 5]
getallen_lijst_filtered
# %%
getallen_lijst_filtered = [getal if getal > 5 else None for getal in getallen_lijst ] 
getallen_lijst_filtered

# %%
getallen_lijst_high = [getal for getal in getallen_lijst if getal > 5] 
getallen_lijst_low  = [getal for getal in getallen_lijst if getal <= 5] 

print(getallen_lijst_high)
print(getallen_lijst_low)

# %%
namen_lijst = ['arie', 'peter', 'jaap', 'gert', 'jan', 'piet', 'klaas']

for naam in namen_lijst:
    print(naam)

# %% 'break' stopt de gehele loop
for naam in namen_lijst:
    if naam == 'jaap':
        print(f"We hebben {naam} gevonden!")
        break
    print(naam)

print("De rest van de code")
# %% 'continue' stopt met de huidige iteratie

for naam in namen_lijst:
    print(naam)
    print("*"*10)
    if naam == 'jaap':
        print("Stop hier maar")
        continue

    print("De rest van de code")
    print("-"*10)
    print(naam.upper())
    print(naam.capitalize())
    print("-"*10)

print("De code na mijn loop")


#%%
i = 0
max = 10

while i < max:
    print(i)
    i += 1


# %%
for i in range(10):
    print(i)
# %%
persoon_dict = {}

persoon_dict['naam'] = 'Arie'
persoon_dict['leeftijd'] = 18
persoon_dict['woonplaats'] = 'Amsterdam'

#%%
persoon_dict['naam']
# %%
