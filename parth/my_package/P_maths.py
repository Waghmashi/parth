import math


def p_calc_factorial():
    num = int(input("enter a number Whose Factorial you Want:"))
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial:{result}")


def p_compound_amount():
    principal = float(input("Enter Principal Amount :"))
    rate = float(input("Enter Rate Of Interest (in %) :"))
    time = int(input("Enter Time (in years) :"))

    total = principal * pow((1 + rate / 100), time)
    print(f"Compound Interest :{total}")


def p_trigo_values():
    angle = float(input("Enter the number in degree :"))
    rad = angle * (math.pi / 180)

    print(f"Degree {angle} sin is :{math.sin(rad)}")
    print(f"Degree {angle} cos is :{math.cos(rad)}")
    print(f"Degree {angle} tan is :{math.tan(rad)}")



def p_area_circle():
    r = float(input("Enter radius:"))
    print(f"Area of circle: {math.pi * r * r}")



def p_area_rectangle():
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print(f"Area of rectangle: {l * w}")

def p_area_triangle():
    b = float(input("Enter base : "))
    h = float(input("Enter height : "))
    print(f"Area of triangle: {0.5 * b * h}")

def p_square_number():
    n = float(input("Enter Num:"))
    print(f"Square of num is:{n ** 2}")

def p_geometry_menu():
    print("Area Of Geomatric Shapes")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    print("4. Square ")
    print("5. Exit from Area of Geomatric")

    while True:
        choice = int(input("Enter Your Choice:"))

        if choice == 1:
            p_area_circle()
        elif choice == 2:
            p_area_rectangle()
        elif choice == 3:
            p_area_triangle()
        elif choice == 4:
            p_square_number()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice")
