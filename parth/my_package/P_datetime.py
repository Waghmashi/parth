import datetime
import time


def p_show_now():
    today = datetime.datetime.now()
    formatted = today.strftime("%d-%m-%Y %I:%M:%S %p")
    print("Current Date and Time :", formatted)



def p_days_gap():
    try:
        start = input("Enter First Date (yyyy-mm-dd): ")
        end = input("Enter Second Date (yyyy-mm-dd): ")

        d1 = datetime.date.fromisoformat(start)
        d2 = datetime.date.fromisoformat(end)

        days = (d2 - d1).days
        print(f"Difference: {days} days")

    except:
        print("Invalid date ! please enter like format.")


def p_display_format():
    print("Date Formatting:")
    print("1. DD/MM/YYYY")
    print("2. MM-DD-YYYY")
    print("3. Full date & time")
    print("4. Day name format")

    option = input("Enter your choice: ")
    current = datetime.datetime.now()

    if option == "1":
        print("Date:", current.strftime("%d/%m/%Y"))
    elif option == "2":
        print("Date:", current.strftime("%m-%d-%Y"))
    elif option == "3":
        print("Date & Time:", current.strftime("%Y/%m/%d %H:%M:%S"))
    elif option == "4":
        print("Date:", current.strftime("%A, %B %d, %Y"))
    else:
        print("Invalid choice.")



def p_run_timer():
    total = int(input("Enter how many seconds to run stopwatch:-"))
    count = 0

    while count <= total:
        print(f"\rRunning Time: {count} seconds", end="")
        time.sleep(1)
        count += 1

    print("\nStopwatch stopped!")



def p_reverse_timer():
    sec = int(input("Enter countdown time in seconds: "))

    while sec >= 0:
        print(f"\rTime Left: {sec} seconds", end="")
        time.sleep(1)
        sec -= 1

    print("\nCountdown finished!")
