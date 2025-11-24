print("Welcome to the Pattern Generator and Number Analyzer!")
while True:
    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    s = int(input("Enter your choice: "))
    
    match s:
        case 1:
            while True:
                i = int(input("Enter the number of rows for the pattern: "))
                if i > 0:
                    break
                print("Please enter a positive number!")
            
            print(f"\nRight-angled Triangle ({i} rows):")
            for j in range(1, i + 1):
                for k in range(1, j + 1):
                    print("*", end=" ")
                print()
        case 2:
            while True:
                r = int(input("Enter the start of the range: "))
                o = int(input("Enter the end of the range: "))
                if o > r:
                    break
                print("End must be greater than start!")
            
            sum_numbers = 0
            odd_count = 0
            even_count = 0
            
            print(f"\nAnalyzing numbers from {r} to {o}:")
            for p in range(r, o + 1):
                sum_numbers += p
                
                if p % 2 == 0:
                    print(f"Number {p} is Even")
                    even_count += 1
                    pass  
                else:
                    print(f"Number {p} is Odd")
                    odd_count += 1
                    continue  
                
                if even_count >= 3 and odd_count >= 3:
                    print("Reached 3 even and 3 odd numbers - stopping early!")
                    break
            print(f"\nSum of all numbers from {r} to {o}: {sum_numbers}")
            print(f"Total even numbers: {even_count}")
            print(f"Total odd numbers: {odd_count}")
        case 3:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice! Please enter 1, 2, or 3.")