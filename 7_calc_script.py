from our_functions.calc_functions import calculate_pythagoras



if __name__ == "__main__":
    value_a = float(input("Give the value of A:\n"))
    value_b = float(input("Give the value of B:\n"))    

    value_c = calculate_pythagoras(value_a, value_b)    
    
    print(__name__)
    print(f"The value of C is {value_c}")
