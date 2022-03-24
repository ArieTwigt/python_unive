#%% importeer de os library
import os

# %% maak een map aan 
os.mkdir("my_folder")

# %% verwijder een file
os.remove("my_file.txt")

# %% geef de bestanden aan in de huidige working directory
os.listdir()
# %% geef de huidige working directory aan
os.getcwd()

# %% geef de bestanden weer in de betreffende folder
current_files = os.listdir('my_folder')
