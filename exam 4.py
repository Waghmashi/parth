global_summary = {"total_values": 0, "overall_mean": 0.0}

def display_data_summary(data):
    if not data:
        print("No data available.")
        return None, None, None, None

    total = len(data)
    max_val = max(data)
    min_val = min(data)
    total_sum = sum(data)
    avg = total_sum / total

    print(f"Total elements: {total}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    print(f"Sum of all values: {total_sum}")
    print(f"Average value: {avg:.2f}")

    global global_summary
    global_summary["total_values"] = total
    global_summary["overall_mean"] = avg
    return min_val, max_val, total_sum, avg

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def filter_data(data, threshold, above=True):
    if above:
        return list(filter(lambda x: x >= threshold, data))
    else:
        return list(filter(lambda x: x < threshold, data))

def sort_data(data, ascending=True):
    return sorted(data) if ascending else sorted(data, reverse=True)

def print_dataset_stats(*args, **kwargs):
    print("Dataset Statistics:")
    for key, value in kwargs.items():
        print(f"- {key.replace('_', ' ').title()}: {value}")
    if args:    
        print("Additional info:", args)

def display_2d_grid(data_2d):
    for row in data_2d:
        print("  ".join(str(x) for x in row))

def input_1d():
    print("Enter data for 1D array (separated by spaces):")
    try:
        return list(map(float, input().split()))
    except:
        print("Invalid input. Using sample data.")

def input_2d():
    print("Enter number of rows:")
    try:
        rows = int(input())
        data = []
        for i in range(rows):
            print(f"Row {i+1} (space-separated):")
            data.append(list(map(float, input().split())))
        return data
    except:
        print("Invalid input. Using sample 2D data.")
        return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def main():
    data_1d = []
    data_2d = []
    data_type = "1D"

    while True:
        print("\n" + "="*50)
        print("DATA ANALYZER AND TRANSFORMER")
        print("="*50)
        print("1. Input Data (1D or 2D)")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (*args, **kwargs)")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Choose data type:\n1. 1D List\n2. 2D List")
            dtype = input("Choice: ").strip()
            if dtype == "1":
                data_1d = input_1d()
                data_type = "1D"
            elif dtype == "2":
                data_2d = input_2d()
                data_type = "2D"
            else:
                print("Invalid choice.")
            print("Data stored successfully.")

        elif choice == "2":
            if data_type == "1D" and data_1d:
                display_data_summary(data_1d)
            elif data_type == "2D" and data_2d:
                flat = [item for row in data_2d for item in row]
                display_data_summary(flat)
            else:
                print("No data available. Input data first.")

        elif choice == "3":
            try:
                n = int(input("Enter a number for factorial: "))
                if n < 0:
                    print("Enter non-negative integer.")
                else:
                    print(f"Factorial of {n} is: {calculate_factorial(n)}")
            except:
                print("Invalid input.")

        elif choice == "4":
            if data_type == "1D" and data_1d:
                try:
                    th = float(input("Enter threshold: "))
                    above = input("Filter values >= threshold? (y/n): ").lower() == 'y'
                    filtered = filter_data(data_1d, th, above)
                    print("Filtered Data:", filtered)
                except:
                    print("Invalid input.")
            else:
                print("Only for 1D data.")

        elif choice == "5":
            if data_type == "1D" and data_1d:
                order = input("Sort ascending? (y/n): ").lower() == 'y'
                sorted_list = sort_data(data_1d, order)
                print("Sorted Data:", sorted_list)
            else:
                print("Only for 1D data.")

        elif choice == "6":
            if data_type == "1D" and data_1d:
                minv, maxv, sumv, avgv = display_data_summary(data_1d)
                print_dataset_stats(
                    min_value=minv,
                    max_value=maxv,
                    sum=sumv,
                    average=avgv
                )
            else:
                print("No 1D data available.")

        elif choice == "7":
            print("Thank you for using the Data Analyzer. Goodbye!")
            break   

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
