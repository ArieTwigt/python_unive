import math

def calculate_pythagoras(a: float, b: float, rounding: int=1, multiplier: int=1, return_sqrd: bool=False) -> float:
    '''

    A function to apply the Pythagoras theorem to calculate the length of the hypotenuse of a right triangle.

    :param a: side a of the triangle (int, float)
    :param b: side b of the triangle (int, float)
    
    :return: length of the hypotenuse (int, float)
    
    
    '''
    print("The name of this script")
    print(__name__)
    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)

    c_rounded = round(c, rounding) * multiplier
    if return_sqrd:
        return c_rounded, c_sqrd
    else:
        return c_rounded