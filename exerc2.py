# import complex math module
import cmath

def calculate_equation_roots(a,b,c):
    """
    calculate the roots of equation ax^2 + bx + c
    :param a: equation ax^2 + bx + c
    :param b: equation ax^2 + bx + c
    :param c: equation ax^2 + bx + c
    :return: the roots of equation ax^2 + bx + c or empty array if equation has no real roots
    """
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    
    x1 = (-b+cmath.sqrt(d))/(2*a)
    x2 = (-b-cmath.sqrt(d))/(2*a)

    # return null if the imaginary part of x1 and x2 are != 0.0
    if x1.imag != 0.0 and x2.imag != 0.0:
        return []
    
    # return the solutions
    return [x1.real, x2.real]

print(calculate_equation_roots(4,3,2))