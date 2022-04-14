from our_functions.rdw_functions import *
import sys
import argparse

# define the argument parser
parser = argparse.ArgumentParser()

# add arguments to parser
parser.add_argument("--brand", type=str, required=True)
parser.add_argument("--amount", type=int, default=1000)

# parse arguments
args = parser.parse_args()

# define variables
selected_brand = args.brand
amount         = args.amount

# get the list of brands
brands_list = show_different_brands()

# choose a function based on the input for 'brand'
if selected_brand == "RANDOM":
    print("No brand selected, getting random cars...")
    cars = get_random_cars()
else:
    cars = get_car_by_brand(selected_brand, num_results=amount)

# export the car list
export_cars_to_csv(cars, brand=selected_brand)

