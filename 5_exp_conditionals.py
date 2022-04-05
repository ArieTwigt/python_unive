#%%
leeftijd = 16 

leeftijds_grens = 17

#%%
if leeftijd < leeftijds_grens:
    print("Je bent nog niet volwassen")
    if leeftijd == 15:
        print("Kindercola")
else:
    print("Je bent volwassen")


# %%

leeftijd = 16

if leeftijd < leeftijds_grens:
    print("Je bent niet volwassen")
elif 15 < leeftijd < 18:
    print("Je krijg shandy") 
else:
    print("Proost")


# %%
if leeftijd >= leeftijds_grens:
    print("Je bent volwassen")


if leeftijd < leeftijds_grens:
    print("Je bent niet volwassen")
else:
    print("Helaas, je bent volwassen")


#%%
gasten_lijst = ['Arie', 'Peter', 'Stef', 'Jeroen', 'Kees', 'Jos', 'Bart', 'Klaas']

naam = 'Martin'


if naam not in gasten_lijst:
    print("Welkom")
else:
    print("Sorry, je bent niet geaccepteerd")

# %% in-line conditional statements
leeftijd_status = "Volwassen" if leeftijd > 18 else "Niet volwassen"
gast_status     = "Geaccepteerd" if naam \
    in gasten_lijst else "Niet geaccepteerd"

#%%
if leeftijd > 18:
    leeftijd_status = "Volwassen"
else:
    leeftijd_status = "Niet volwassen"