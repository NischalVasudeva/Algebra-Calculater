
def Run_Linear():

    print('Equation 1')

    A1 = int(input("A="))
    B1 = int(input("B="))
    C1 = int(input("C="))

    print('Equation 2')

    A2 = int(input("A="))
    B2 = int(input("B="))
    C2 = int(input("C="))



    print(f"Find the solution of {A1}x+{B1}y={C1}")

    print(f"and {A2}x+{B2}y={C2}")


    #step 1


    print((f"+{B1}y={C1}+{A1*-1}x"))

    A1 = A1/B1

    C1 = C1/B1

    A1=A1*-1
    print((f"+y={C1}+{A1}x"))

    print((f"+{B2}y={C2}+{A2 * -1}x"))

    new_A2 = A2 / B2

    new_C2 = C2 / B2

    new_A2 = new_A2 * -1
    print((f"+y={new_C2}+{new_A2}x"))

    if A1==new_A2 and new_C2!=C1:
        print('No Solution')
        return""

    #step 2


    print((f"+{A2}x={C2}+{B2*-1}y"))

    B2 = B2/A2

    C2 = C2/A2

    B2=B2*-1
    print((f"+x={C2}+{B2}y"))



    #step 3
    print(f"Y={C1}+{A1}({C2}+{B2}y)")


    new_y = 1+(A1*(B2*-1))


    yvalue= C1+(A1*C2)

    if new_y == 0:
        print('Infinite Solutions')
        return ""

    y = yvalue/new_y
    y = round(y, 3)



    print(f"y={y}")


    #step4

    x = C2+(B2*y)
    x=round(x, 3)
    print(f"x={x}")



    print(f"{x}, {y}")


