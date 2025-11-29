# Student Data Organizer
# A comprehensive student record management system

class StudentDataOrganizer:
    def __init__(self):
        self.students_list = []  # List to store all student records
        self.students_dict = {}  # Dictionary with student ID as key
        self.all_subjects = set()  # Set to store unique subjects
        
    def display_welcome_message(self):
        """Display welcome message and program overview"""
        print("=" * 50)
        print("    WELCOME TO STUDENT DATA ORGANIZER")
        print("=" * 50)
        print("This program helps you manage student records efficiently.")
        print("You can add, view, update, and delete student information.")
        print("All data is stored using appropriate collection types.")
        print("-" * 50)
    
    def get_student_input(self):
        """Collect student information from user input"""
        print("\n--- Enter Student Details ---")
        
        # Using different string formatting methods as required
        student_id = input("Student ID: ").strip()
        name = input("Name: ").strip()
        age = input("Age: ").strip()
        grade = input("Grade: ").strip()
        dob = input("Date of Birth (YYYY-MM-DD): ").strip()
        
        # Using % formatting
        subjects_input = input("Subjects (comma-separated): ").strip()
        
        # Type casting for age
        try:
            age = int(age)
        except ValueError:
            print("Invalid age! Setting age to 0.")
            age = 0
        
        # Process subjects and add to set
        subjects = [subject.strip() for subject in subjects_input.split(",") if subject.strip()]
        subjects_set = set(subjects)
        
        # Update global subjects set
        self.all_subjects.update(subjects_set)
        
        # Create immutable tuple for ID and DOB
        id_dob_tuple = (student_id, dob)
        
        # Create student dictionary
        student_data = {
            'name': name,
            'age': age,
            'grade': grade,
            'subjects': subjects,
            'id_dob': id_dob_tuple
        }
        
        return student_id, student_data
    
    def add_student(self):
        """Add a new student record"""
        student_id, student_data = self.get_student_input()
        
        # Add to list (demonstrating list mutability)
        self.students_list.append({'id': student_id, **student_data})
        
        # Add to dictionary
        self.students_dict[student_id] = student_data
        
        # Using f-string formatting
        print(f"\n✓ Student {student_data['name']} (ID: {student_id}) added successfully!")
    
    def display_all_students(self):
        """Display all student records using formatted output"""
        if not self.students_list:
            print("\nNo student records found!")
            return
        
        print("\n" + "=" * 80)
        print("                           ALL STUDENT RECORDS")
        print("=" * 80)
        print(f"{'ID':<8} {'Name':<15} {'Age':<4} {'Grade':<6} {'Subjects':<30} {'Date of Birth':<12}")
        print("-" * 80)
        
        for student in self.students_list:
            # Using format() method for string formatting
            subjects_str = ", ".join(student['subjects'])
            dob = student['id_dob'][1]
            
            print("{:<8} {:<15} {:<4} {:<6} {:<30} {:<12}".format(
                student['id'], student['name'], student['age'], 
                student['grade'], subjects_str, dob
            ))
        
        print("=" * 80)
    
    def update_student(self):
        """Update student information"""
        if not self.students_dict:
            print("\nNo student records to update!")
            return
        
        student_id = input("\nEnter Student ID to update: ").strip()
        
        if student_id not in self.students_dict:
            print("Student ID not found!")
            return
        
        student = self.students_dict[student_id]
        
        print(f"\nCurrent information for {student['name']}:")
        print(f"1. Age: {student['age']}")
        print(f"2. Grade: {student['grade']}")
        print(f"3. Subjects: {', '.join(student['subjects'])}")
        
        choice = input("\nWhat would you like to update? (1-3): ").strip()
        
        if choice == '1':
            new_age = input("Enter new age: ").strip()
            try:
                # Type casting
                student['age'] = int(new_age)
                print("Age updated successfully!")
            except ValueError:
                print("Invalid age format!")
                
        elif choice == '2':
            new_grade = input("Enter new grade: ").strip()
            student['grade'] = new_grade
            print("Grade updated successfully!")
            
        elif choice == '3':
            new_subjects = input("Enter new subjects (comma-separated): ").strip()
            subjects_list = [subject.strip() for subject in new_subjects.split(",") if subject.strip()]
            
            # Update student's subjects
            student['subjects'] = subjects_list
            
            # Update global subjects set
            self.all_subjects.update(subjects_list)
            print("Subjects updated successfully!")
            
        else:
            print("Invalid choice!")
            return
        
        # Update the list as well (demonstrating list mutability)
        for i, std in enumerate(self.students_list):
            if std['id'] == student_id:
                self.students_list[i] = {'id': student_id, **student}
                break
    
    def delete_student(self):
        """Delete a student record using del keyword"""
        if not self.students_dict:
            print("\nNo student records to delete!")
            return
        
        student_id = input("\nEnter Student ID to delete: ").strip()
        
        if student_id not in self.students_dict:
            print("Student ID not found!")
            return
        
        student_name = self.students_dict[student_id]['name']
        
        # Using del keyword to delete from dictionary
        del self.students_dict[student_id]
        
        # Remove from list
        for i, student in enumerate(self.students_list):
            if student['id'] == student_id:
                # Using del with list index
                del self.students_list[i]
                break
        
        print(f"\n✓ Student {student_name} (ID: {student_id}) deleted successfully!")
    
    def display_subjects(self):
        """Display all unique subjects using set"""
        if not self.all_subjects:
            print("\nNo subjects available!")
            return
        
        print("\n" + "=" * 40)
        print("        UNIQUE SUBJECTS OFFERED")
        print("=" * 40)
        
        # Display subjects in alphabetical order
        for i, subject in enumerate(sorted(self.all_subjects), 1):
            print(f"{i}. {subject}")
        
        print("=" * 40)
        print(f"Total unique subjects: {len(self.all_subjects)}")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 50)
        print("             MAIN MENU")
        print("=" * 50)
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        print("-" * 50)
    
    def run(self):
        """Main program loop"""
        self.display_welcome_message()
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_all_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.display_subjects()
            elif choice == '6':
                self.exit_program()
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")
    
    def exit_program(self):
        """Display exit message"""
        print("\n" + "=" * 50)
        print("    THANK YOU FOR USING STUDENT DATA ORGANIZER!")
        print("=" * 50)
        print("Shaping 'skills' for 'scaling' higher...!!!")
        print("Quality is our Motto.")
        print("-" * 50)


# Main execution
if __name__ == "__main__":
    try:
        organizer = StudentDataOrganizer()
        organizer.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")