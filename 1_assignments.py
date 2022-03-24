# Voorbeeldcode 
from unicodedata import name


https://github.com/ArieTwigt/python_unive



# 1. Maak de volgende variabelen aan met je naam
voornaam = "Arie"
achternaam = "Twigt"

# Zorg ervoor dat er 'Jr.' achter je naam staat:
# 'Arie Twigt Jr.' Wijs dit toe aan een nieuwe variable 'volledige_naam'


# 2. Vervang je volledige voornaam alleen door de eerste letter van je voornaam
# Wijs dit door aan een nieuwe variabele volledige_naam_short
# 'A. Twigt Jr.'


# 3. Maak de volgende lijst met namen aan
namen_lijst = ['John', 'Jim', 'Ann', 'Mary', 'Eric']

# vervang de naam 'Jim' voor 'Arie'


# voeg de naam 'Dirk' toe aan de lijst


### Oplossingen
## 1
#%% 
voornaam = "Arie"
achternaam = "Twigt"
volledige_naam = f"{voornaam} {achternaam} Jr."
print(volledige_naam)

## 2
#%% a
voornaam_short = voornaam.replace("rie", ".")
volledige_naam_short = f"{voornaam_short} {achternaam} Jr."
print(volledige_naam_short)


#%% b
volledige_naam_short = f"{voornaam[0]}. {achternaam} Jr."
print(volledige_naam_short)

## 3.

# %%
namen_lijst = ['John', 'Jim', 'Ann', 'Mary', 'Eric']
namen_lijst[1] = 'Arie'
namen_lijst.append('Dirk')
print(namen_lijst)
# %%
['Unkown' if naam != 'Eric' else naam for naam in namen_lijst]
# %%
