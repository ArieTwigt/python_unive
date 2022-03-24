#%% importeer de datetime modulee
import datetime

# %% geef het huidige datum en tijdstip
datetime.datetime.now()

# %% geef de huidige datum
datetime.date.today()

# %% wijs huidige datum toe aan variabele
current_date = datetime.date.today()

#%%
current_date_str = str(current_date)

# %%
f"Ik ben op {current_date} in Zwolle"

# %%
"Ik ben in Zwolle op" + current_date_str

# %%
my_birthday = datetime.date(1995, 12, 25)

# %%
year_month = my_birthday.strftime("%Y/%m")

# %%
first_date = datetime.date(2024,3,28)

#%%
time_difference = first_date - current_date
# %%
day_difference = time_difference.days

# %% weeknummer ophalen
first_date.isocalendar()[1]



# %%
