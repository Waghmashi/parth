from my_package import P_datetime
from my_package import P_fileOp
from my_package import P_maths
from my_package import P_Random
from my_package import p_uuid



def mainmenu():
    print("Welcome to Multi-Utility Toolkit")
    

    while True:
        print("\nChoose an Option :")
        print("1. Datetime And Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Exit")
       

        try:
            choice = int(input("Enter Your Choice :"))

            if choice == 1:
                datetime_menu()

            elif choice == 2:
                maths_menu()

            elif choice == 3:
                random_menu()

            elif choice == 4:
                print("\nGenerate Unique Identifier:\n")
                p_uuid.UniqueID()

            elif choice == 5:
                file_menu()

            elif choice == 6:
                print("Thank You For Using the Multi-Utility Toolkit !")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please Enter a Valid Number")


def datetime_menu():
    while True:
        print("\nDate and Time Operations:")
        print("1. Display current Date and Time")
        print("2. Calculate difference between Two Dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        try:
            ch = int(input("Enter Your Choice: "))

            if ch == 1:
                P_datetime.p_show_now()

            elif ch == 2:
                P_datetime.p_days_gap()

            elif ch == 3:
                P_datetime.p_display_format()

            elif ch == 4:
                P_datetime.p_run_timer()

            elif ch == 5:
                P_datetime.p_reverse_timer()

            elif ch == 6:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter valid number only")



def maths_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Values")
        print("4. Area of Shapes")
        print("5. Back")

        try:
            ch = int(input("Enter Your Choice: "))

            if ch == 1:
                P_maths.p_calc_factorial()

            elif ch == 2:
                P_maths.p_compound_amount()

            elif ch == 3:
                P_maths.p_trigo_values()

            elif ch == 4:
                P_maths.p_geometry_menu()

            elif ch == 5:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter valid number only")


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back")

        try:
            ch = int(input("Enter Your Choice: "))

            if ch == 1:
                P_Random.p_generate_number()

            elif ch == 2:
                P_Random.p_generate_list()

            elif ch == 3:
                P_Random.p_generate_password()

            elif ch == 4:
                P_Random.p_generate_otp()

            elif ch == 5:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter valid number only")


def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        try:
            ch = int(input("Enter Your Choice: "))

            if ch == 1:
                P_fileOp.p_create_text()

            elif ch == 2:
                P_fileOp.p_write_text()

            elif ch == 3:
                P_fileOp.p_read_text()

            elif ch == 4:
                P_fileOp.p_append_text()

            elif ch == 5:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter valid number only")



mainmenu()
