print("Welcome to the Student Data Organizer!")

students_list = []
students_dict = {}
subjects_set = set()

while True:
    print("Select Option:")
    print("\n1. Add Students\n2. Display All\n3. Update Student\n4. Delete Student\n5. Display Subjects\n6. Exit")
    choice = input("Enter choice (1-7): ")
    
    match choice:
      
        
        case '1':
            print("\n--- Add Students ---")
            try:
                num_students = int(input("How many students do you want to add? "))
                if num_students <= 0:
                    print("Please enter a positive number!")
                    continue
            except:
                print("Invalid number!")
                continue
            
            for i in range(num_students):
                print(f"\n--- Adding Student {i+1}/{num_students} ---")
                try:
                    student_id = int(input("Student ID: "))
                    if student_id in students_dict:
                        print("Error: ID exists! Skipping this student.")
                        continue
                except:
                    print("Error: Invalid ID! Skipping this student.")
                    continue
                    
                name = input("Name: ")
                try:
                    age = int(input("Age: "))
                except:
                    print("Error: Invalid age! Skipping this student.")
                    continue
                    
                grade = input("Grade: ")
                dob = input("DOB (YYYY-MM-DD): ")
                subjects = [s.strip() for s in input("Subjects (comma-separated): ").split(',')]
                
                id_dob_tuple = (student_id, dob)
                student_data = {'name': name, 'age': age, 'grade': grade, 'subjects': subjects, 'id_dob': id_dob_tuple}
                
                students_list.append(student_data)
                students_dict[student_id] = student_data
                subjects_set.update(subjects)
                
                print(f"Student {student_id} added successfully!")
            
            print(f"\nTotal {num_students} students added successfully!")
        
        case '2':
            print("\n--- All Students ---")
            if not students_list:
                print("No records!")
            else:
                print(f"Total Students: {len(students_list)}")
                for student in students_list:
                    sid = student['id_dob'][0]
                    print(f"ID: {sid} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
                    print("Subjects: " + ", ".join(student['subjects']))
                    print("-" * 50)
        
        case '3':
            print("\n--- Update Student ---")
            if not students_dict:
                print("No records!")
                continue
            try:
                sid = int(input("Enter ID to update: "))
                if sid not in students_dict:
                    print("ID not found!")
                    continue
            except:
                print("Invalid ID!")
                continue
                
            student = students_dict[sid]
            print(f"1. Name: {student['name']}\n2. Age: {student['age']}\n3. Grade: {student['grade']}\n4. Subjects: {student['subjects']}")
            field = input("Field to update (1-4): ")
            
            match field:
                case '1':
                    student['name'] = input("New name: ")
                case '2':
                    try:
                        student['age'] = int(input("New age: "))
                    except:
                        print("Invalid age!")
                case '3':
                    student['grade'] = input("New grade: ")
                case '4':
                    new_subjects = [s.strip() for s in input("New subjects: ").split(',')]
                    student['subjects'] = new_subjects
                    subjects_set.update(new_subjects)
                case _:
                    print("Invalid choice!")
        
        case '4':
            print("\n--- Delete Student ---")
            if not students_dict:
                print("No records!")
                continue
            try:
                sid = int(input("Enter ID to delete: "))
                if sid not in students_dict:
                    print("ID not found!")
                    continue
            except:
                print("Invalid ID!")
                continue
                
            del students_dict[sid]
            for i, s in enumerate(students_list):
                if s['id_dob'][0] == sid:
                    del students_list[i]
                    break
            print(f"Student {sid} deleted!")
        
        case '5':
            print("\n--- All Subjects ---")
            if subjects_set:
                print(f"Total Unique Subjects: {len(subjects_set)}")
                for i, sub in enumerate(sorted(subjects_set), 1):
                    print(f"{i}. {sub}")
            else:
                print("No subjects!")
        
        case '6':
            print("\nThank you for using Student Data Organizer!")
            break
        
        case _:
            print("Invalid choice!")