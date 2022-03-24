# 1. Maak een variable aan die het aantal dagen tot en met
# kerst weergeeft

#%% 
import datetime

current_date          = datetime.date.today()
christmas_date        = datetime.date(2022,12,25)
date_difference       = christmas_date - current_date
days_until_christmas = date_difference.days
print(days_until_christmas)

# 2. Bedenk de code die de oppervlakte van een 
# cirkel berekend met een diameter van 10 (straal kwadraat * pi)

#%% 
import math

diameter = 10
straal   = diameter/2
oppervlakte = math.pi * math.pow(straal, 2)
print(oppervlakte)

# 3. Creeer een lijst die de bestanden in je huidige 
# projectmap bevat
#%%
import os

current_files_folders = os.listdir()
print(current_files_folders)


# 4. Maak vanuit Python (os) een extra map aan 'our_functions'
# %%
os.mkdir("our_functions")
# %%
