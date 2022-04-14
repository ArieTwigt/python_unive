#%%
import json


#%%
config_dict = {}
config_dict['db_loc'] = 'https://my_db.loc'
config_dict['brands'] = ['OPEL', 'TOYOTA', 'NISSAN']
config_dict['limit']  = 5000

#%%
config_str = json.dumps(config_dict)


# %%
with open("config.json", "w") as file:
    file.write(config_str)
# %%
