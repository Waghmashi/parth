print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\n1. Generate pattern\n2. Analyze numbers\n3. Exit")
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            rows = int(input("Enter rows: "))
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()
        
        case 2:
            start = int(input("Start: "))
            end = int(input("End: "))
            total = 0
            
            for num in range(start, end + 1):
                total += num
                
                if num % 2 == 0:
                    pass  
                else:
                    pass  
                    
            
                if num % 10 == 0:
                    continue
                    
            print(f"Sum: {total}")
            
            
            count = start
            while count <= end:
                if count > start + 5:
                    break
                print(count, end=" ")
                count += 1
            print()
        
        case 3:
            print("Goodbye!")
            break
        
        case _:
            pass