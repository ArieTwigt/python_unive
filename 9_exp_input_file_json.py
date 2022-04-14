#%%
from our_functions.rdw_functions import *
import json
from tqdm import tqdm

#%% 
with open("config.json", "r") as file:
    config_str = file.read()


# %%
config_dict = json.loads(config_str)

# %%
brands_list = config_dict['brands']
limit       = config_dict['limit']

# %%
for brand in tqdm(brands_list):
    cars_list = get_car_by_brand(brand=brand, num_results=limit)
    export_cars_to_csv(cars_list, brand)
