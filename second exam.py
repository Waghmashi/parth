def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print("="*50)
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

def generate_pattern():
    """Generate a right-angled triangle pattern"""
    try:
        rows = int(input("Enter the number of rows for the pattern: "))
        
        if rows <= 0:
            print("Error: Number of rows must be positive!")
            return
        
        print("\nPattern:")
        for i in range(1, rows + 1):
            print('*' * i)
            
    except ValueError:
        print("Error: Please enter a valid integer!")

def analyze_numbers():
    """Analyze a range of numbers"""
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        if end <= start:
            print("Error: End of range must be greater than start!")
            return
        
        total_sum = 0
        
        print()
        for num in range(start, end + 1):
            # Determine if number is odd or even
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            
            total_sum += num
        
        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")
        
    except ValueError:
        print("Error: Please enter valid integers!")

def main():
    """Main program loop"""
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                generate_pattern()
            elif choice == 2:
                analyze_numbers()
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1, 2, or 3.")
                
        except ValueError:
            print("Error: Please enter a valid number!")

# Run the program
if __name__ == "__main__":
    main()