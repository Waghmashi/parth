dataset_summary = {
    'total_values': 0,
    'overall_mean': 0.0,
    'dataset_type': 'None'
}
data_1d = []
data_2d = []
current_data_type = '1D'  
def print_separator():
    print("\n" + "="*60)
def display_data():
    print("CURRENT DATASET:")
    if current_data_type == '1D' and data_1d:
        print(f"1D Array: {data_1d}")
    elif current_data_type == '2D' and data_2d:
        print("2D Array (Grid Format):")
        for row in data_2d:
            print("  " + "  ".join(str(val) for val in row))
    else:
        print("No data loaded. Please input data first.")

def display_data_summary():
    print_separator()
    print("DATA SUMMARY (Using Built-in Functions):")
    if current_data_type == '1D' and data_1d:
        if data_1d:
            print(f"- Total elements: {len(data_1d)}")
            print(f"- Minimum value: {min(data_1d)}")
            print(f"- Maximum value: {max(data_1d)}")
            print(f"- Sum of all values: {sum(data_1d)}")
            print(f"- Average value: {sum(data_1d)/len(data_1d):.2f}")
        else:
            print("No data available.")
    elif current_data_type == '2D' and data_2d:
        all_values = []
        for row in data_2d:
            all_values.extend(row)
            if all_values:          
            print(f"- Total elements: {len(all_values)}")
            print(f"- Minimum value: {min(all_values)}")
            print(f"- Maximum value: {max(all_values)}")
            print(f"- Sum of all values: {sum(all_values)}")
            print(f"- Average value: {sum(all_values)/len(all_values):.2f}")
        else:
            print("No data available.")
    else:
        print("No data loaded. Please input data first.")
def calculate_average(data_list):
    if not data_list:
        return 0
    return sum(data_list) / len(data_list)

def find_duplicates(data_list):
    seen = set()
    duplicates = set()
    
    for value in data_list:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    
    return list(duplicates)

def display_unique_values(data_list):
    unique_values = set(data_list)
    print(f"Unique values: {sorted(unique_values)}")
def recursion_operations():
    print_separator()
    print("RECURSION OPERATIONS:")
    print("1. Calculate Factorial")
    print("2. Calculate Fibonacci Number")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == '1':
        try:
            num = int(input("Enter a number to calculate its factorial: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                result = factorial_recursive(num)
                print(f"Factorial of {num} is: {result}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    elif choice == '2':
        try:
            num = int(input("Enter position in Fibonacci sequence: "))
            if num < 0:
                print("Position must be non-negative.")
            else:
                result = fibonacci_recursive(num)
                print(f"Fibonacci number at position {num} is: {result}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    else:
        print("Invalid choice.")

def filter_with_lambda(threshold, above=True):
    if current_data_type == '1D' and data_1d:
        if above:
            filter_func = lambda x: x > threshold
            filtered = list(filter(filter_func, data_1d))
            print(f"Values above {threshold}: {filtered}")
        else:
            filter_func = lambda x: x < threshold
            filtered = list(filter(filter_func, data_1d))
            print(f"Values below {threshold}: {filtered}")
        return filtered
    elif current_data_type == '2D' and data_2d:
        all_values = []
        for row in data_2d:
            all_values.extend(row)
        
        if above:
            filter_func = lambda x: x > threshold
            filtered = list(filter(filter_func, all_values))
            print(f"Values above {threshold}: {filtered}")
        else:
            filter_func = lambda x: x < threshold
            filtered = list(filter(filter_func, all_values))
            print(f"Values below {threshold}: {filtered}")
        return filtered
    else:
        print("No data loaded.")
        return []
def lambda_operations():
    print_separator()
    print("LAMBDA FUNCTION OPERATIONS:")
    print("1. Filter Data by Threshold")
    print("2. Map Transformation")
    choice = input("Enter your choice (1-2): ")
    if choice == '1':
        try:
            threshold = float(input("Enter threshold value: "))
            print("Filter option:")
            print("1. Values above threshold")
            print("2. Values below threshold")
            filter_choice = input("Enter choice (1-2): ")
            
            if filter_choice == '1':
                filter_with_lambda(threshold, above=True)
            elif filter_choice == '2':
                filter_with_lambda(threshold, above=False)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice == '2':
        map_with_lambda()
    else:
        print("Invalid choice.")
def get_dataset_stats():
    if current_data_type == '1D' and data_1d:
        min_val = min(data_1d)
        max_val = max(data_1d)
        total_sum = sum(data_1d)
        average = total_sum / len(data_1d)
        return min_val, max_val, total_sum, average
    elif current_data_type == '2D' and data_2d:
        all_values = []
        for row in data_2d:
            all_values.extend(row)
        
        min_val = min(all_values)
        max_val = max(all_values)
        total_sum = sum(all_values)
        average = total_sum / len(all_values)
        return min_val, max_val, total_sum, average
    else:
        return 0, 0, 0, 0

def display_multiple_stats():
    print_separator()
    print("DATASET STATISTICS (Return Multiple Values):")
    
    min_val, max_val, total_sum, average = get_dataset_stats()
    
    if min_val == 0 and max_val == 0 and total_sum == 0:
        print("No data available.")
    else:
        print(f"- Minimum value: {min_val}")
        print(f"- Maximum value: {max_val}")
        print(f"- Sum of all values: {total_sum}")
        print(f"- Average value: {average:.2f}")

def input_1d_data():
    global data_1d, current_data_type
    
    print_separator()
    print("1D DATA INPUT")
    print("Enter data separated by spaces (e.g., '34 12 56 78 43 21 90'):")
    
    try:
        data_str = input("Enter data: ")
        data_1d = [float(x) for x in data_str.split()]
        current_data_type = '1D'
        update_global_summary()
        print(f"Data has been stored successfully! ({len(data_1d)} elements)")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        data_1d = []

def input_2d_data():
    global data_2d, current_data_type
    
    print_separator()
    print("2D DATA INPUT")
    print("Enter number of rows and columns, then enter each row.")
    
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        data_2d = []
        for i in range(rows):
            row_str = input(f"Enter row {i+1} ({cols} values separated by spaces): ")
            row = [float(x) for x in row_str.split()]
            
            if len(row) != cols:
                print(f"Error: Row must have exactly {cols} values.")
                data_2d = []
                return
            
            data_2d.append(row)
        
        current_data_type = '2D'
        update_global_summary()
        print(f"Data has been stored successfully! ({rows}×{cols} matrix)")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        data_2d = []

def use_sample_data():
    global data_1d, data_2d, current_data_type
    
    print_separator()
    print("SAMPLE DATA SELECTION")
    print("1. 1D Sample Data: [34, 12, 56, 78, 43, 21, 90]")
    print("2. 2D Sample Data: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    
    choice = input("Enter choice (1-2): ")
    
    if choice == '1':
        data_1d = [34, 12, 56, 78, 43, 21, 90]
        data_2d = []
        current_data_type = '1D'
        update_global_summary()
        print("1D sample data loaded successfully!")
    elif choice == '2':
        data_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        data_1d = []
        current_data_type = '2D'
        update_global_summary()
        print("2D sample data loaded successfully!")
    else:
        print("Invalid choice.")

def input_data_menu():
    print_separator()
    print("DATA INPUT MENU:")
    print("1. Input 1D Data")
    print("2. Input 2D Data")
    print("3. Use Sample Data")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        input_1d_data()
    elif choice == '2':
        input_2d_data()
    elif choice == '3':
        use_sample_data()
    else:
        print("Invalid choice.")

def sort_1d_data(ascending=True):
    if data_1d:
        if ascending:
            data_1d.sort()
            print("Sorted Data in Ascending Order:")
            print(data_1d)
        else:
            data_1d.sort(reverse=True)
            print("Sorted Data in Descending Order:")
            print(data_1d)
    else:
        print("No 1D data available.")

def sort_2d_data():
    print_separator()
    print("2D DATA SORTING OPTIONS:")
    print("1. Sort each row")
    print("2. Sort by first column")
    print("3. Sort by sum of each row")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        sorted_data = [sorted(row) for row in data_2d]
        print("Sorted 2D Array (each row sorted):")
        for row in sorted_data:
            print("  " + "  ".join(str(val) for val in row))
    elif choice == '2':
        sorted_data = sorted(data_2d, key=lambda x: x[0])
        print("Sorted 2D Array (by first column):")
        for row in sorted_data:
            print("  " + "  ".join(str(val) for val in row))
    elif choice == '3':
        sorted_data = sorted(data_2d, key=lambda x: sum(x))
        print("Sorted 2D Array (by row sum):")
        for row in sorted_data:
            print("  " + "  ".join(str(val) for val in row))
    else:
        print("Invalid choice.")

def sort_operations():
    print_separator()
    print("SORTING OPERATIONS:")
    
    if current_data_type == '1D' and data_1d:
        print("1. Sort in Ascending Order (using sort() method)")
        print("2. Sort in Descending Order (using sort() method)")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            sort_1d_data(ascending=True)
        elif choice == '2':
            sort_1d_data(ascending=False)
        else:
            print("Invalid choice.")
    
    elif current_data_type == '2D' and data_2d:
        sort_2d_data()
    else:
        print("No data loaded.")
            type="1D Array",
            size=len(data_1d),
            min_value=min(data_1d),
            max_value=max(data_1d),
            average=calculate_average(data_1d)
    elif current_data_type == '2D' and data_2d:
        all_values = []
        for row in data_2d:
            all_values.extend(row)
        def main_menu():
    while True:
        print_separator()
        print("WELCOME TO THE DATA ANALYZER AND TRANSFORMER PROGRAM")
        print_separator()
        print("MAIN MENU:")
        print(" 1. Input Data")
        print(" 2. Display Data Summary (Built-in Functions)")
        print(" 3. Calculate factorial Recursive")
        print(" 4. Filter daya by Threshold (Lambda Function)")
        print(" 5. Sort Data")
        print(" 6. Display Dataset Statistics")
        print(" 7. Exit Program")
        print_separator()
        
        display_data()
        print_separator()
        
        choice = input("Please enter your choice (1-11): ")
        
        if choice == '1':
            input_data_menu()
        elif choice == '2':
            display_data()
        elif choice == '3':
            Calculate_factorial()
        elif choice == '4':
            lambda_operations()
        elif choice == '5':
            Sort_data()
        elif choice == '7':
            display_multiple_stats()
        elif choice == '7':
            Exit program()
            print_separator()
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            print_separator()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()