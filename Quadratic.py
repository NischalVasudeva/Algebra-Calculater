import math


def Run_Quadratic():

    A = float(input("A="))
    B = float(input("B="))
    C = float(input("C="))

    try:
        root = math.sqrt(B**2-(4*A*C))
        xint1 = ((-B+root)/(2*A))
        xint2 = ((-B-root)/(2*A))

    except:
        print("Not a valid equation, there is no solution, no x intercepts for this equation.")

    else:
        root = math.sqrt(B ** 2 - (4 * A * C))
        xint1 = ((-B + root) / (2 * A))
        xint2 = ((-B - root) / (2 * A))
        print(f"{xint1},0")
        print(f"{xint2},0")