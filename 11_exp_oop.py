#%%
class Car:
    # attributes
    purpose    = "transport"
    car_status = "Available"
    exported   = False

    # inital attributes
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # methods
    def show_car(self):
        print(f"This is a {self.brand} of type {self.model}")
    

    def car_sold(self):
        self.car_status = "SOLD"

    
    def change_price(self, amount):
        old_price = self.price
        self.price += amount
        print(f"from {old_price} to {self.price}")
        

    def export_file(self):
        explanation = f'''
                       This is a {self.brand}
                       of the type: {self.model}

                       The price is:

                       {self.price}

                       The status is:

                       {self.car_status}
                       '''

        with open("car_explanation.txt", "w") as file:
            file.write(explanation)

        
        self.exported = True


#%%
car_1 = Car("VOLVO", "V70", 10000)


# %%
car_1.change_price(4000)
# %%
car_1.exported
# %%
car_1.export_file()
# %%
