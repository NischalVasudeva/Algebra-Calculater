import math


def Run_Pythag():


    print('Type x if varible is unknown.')


    A = (input("A="))
    B = (input("B="))
    C = (input("C="))


    List = [A, B, C]

    Unknown_Varible = ()

    number = 0

    for var in List:
        number += 1
        if var=='x' or var=="X":
            if number == 1:
                Unknown_Varible = 1

            if number == 2:
                Unknown_Varible = 2

            if number == 3:
                Unknown_Varible = 3





    if Unknown_Varible == 3:
        A = float(A)
        B = float(B)
        C=(A**2)+(B**2)
        C=math.sqrt(C)
        print(f"C={C}")

    if Unknown_Varible == 2:
        A = float(A)
        C = float(C)

        B=((C**2)-(A**2))
        B=math.sqrt(B)
        print(f"B={B}")

    if Unknown_Varible == 1:
        B = float(B)
        C = float(C)

        A=((C**2)-(B**2))
        A=math.sqrt(A)
        print(f"A={A}")





