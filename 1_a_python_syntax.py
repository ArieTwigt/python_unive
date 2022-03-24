#%% Enkelvoudige string
from operator import le
from unicodedata import name


naam = 'Arie'
achternaam = 'Twigt'
#%%
volledige_naam = naam + ' ' + achternaam
print(volledige_naam)

#%%

# %%
volledige_naam = f'Mijn naam is {naam} en mijn \nachternaam is:" {achternaam}.'
print(volledige_naam)
# %% Doc string
mijn_verhaal = '''
Dit is mijn 
lange
verhaal

Met vriendelijke groet,

Arie





'''
# %%
print(mijn_verhaal)


# Speciale methods in Python
#%%
naam = 'Arie'
naam_list = naam.split('r')

#%%
''.join(naam_list)


#%% replace
naam.replace("A", "U")

#%% strip
naam_raw = '   Urie '
naam_clean = naam_raw.lstrip()\
                     .rstrip()\
                     .replace("U", "A")\
                     .upper()
naam_clean

### Numerieke waarden

#%%
leeftijd = 18
lengte = 1.93


#%%
leeftijd + lengte
# %%
leeftijd * 2
# %%

# %%

### Lists

#%%
namen_lijst = ['Arie', 'Jan', 'Dirk']

#%%
naam_2 = 'Gijs'
namen_lijst.append(naam_2)
# %%
namen_lijst
# %%
namen_lijst[0]
# %%



### Dictionaries

#%%
persoon_1 = {'naam': 'Arie', 
             'leeftijd': 40,
             'sporten': ['Voetbal', 'Fietsen', 'Boksen']}

#%%
persoon_1['sporten'][1]



#%% tuples
namen_tuple = ('Arie', 'Jaap', 'Dirk')

#%%
namen_lijst[0] = "Gerrit"
print(namen_lijst)

# Dit is commentaar

# %%
namen_tuple[0] = 'Gerrit'
print(namen_tuple)
# %%
list(namen_tuple)
# %%
namen_lijst_1 = ['Arie', 'Jan', 'Dirk']
namen_lijst_2 = ['Gerrit', 'Kees']

#%%
namen_lijst_1 + namen_lijst_2
# %%
