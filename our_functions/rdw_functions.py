from urllib import response
import requests
import pandas as pd
import os


def show_different_brands():
    endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?$query=SELECT DISTINCT merk"
    response = requests.get(endpoint)
    merken = response.json()
    merken_list = [merk['merk'] for merk in merken]
    merken_str = "\n".join(merken_list)
    return merken_str


def get_random_cars(num_results=1000):
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?$limit={num_results}"
    response = requests.get(endpoint)
    cars_list = response.json()
    return cars_list


def get_car_by_brand(brand, num_results=1000):

    if num_results > 50000:
        raise ValueError(f"{num_results} not possible, max results is 50000")

    brand_upper = brand.upper()
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}&$limit={num_results}" 
    response = requests.get(endpoint)
    cars_list = response.json()
    return cars_list


def export_cars_to_csv(car_list, brand="RANDOM", data_folder= "data"):
    df_cars = pd.DataFrame(car_list)


    # check if directory exists
    files_folders = os.listdir()

    if data_folder not in files_folders:
        print(f"Creating data folder: {data_folder}")
        os.mkdir(data_folder)

    # creating the sub folder
    export_folder = f"{data_folder}/{brand}"
    os.makedirs(export_folder, exist_ok=True)
    
    # exporting the file
    file_name = f"{export_folder}/imported_cars.csv"
    
    df_cars.to_csv(file_name,
                index=False,
                sep=";")
