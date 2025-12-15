class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name="", age=0, employee_id="", salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id  
        self.__salary = salary  
    
    def get_employee_id(self):
        return self.__employee_id
    
    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
    
    @classmethod
    def create_employee(cls, name, age, employee_id="", salary=0.0):
        if employee_id and salary > 0:
            return cls(name, age, employee_id, salary)
        else:
            return cls(name, age)
    
    def display(self):
        super().display()
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary:.1f}")


class Manager(Employee):
    def __init__(self, name="", age=0, employee_id="", salary=0.0, department=""):
        super().__init__(name, age, employee_id, salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")


def main():
    people = []
    
    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                person = Person(name, age)
                people.append(person)
                print(f"\nPerson created with name: {name} and age: {age}.")
            
            case '2':
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                employee = Employee(name, age, emp_id, salary)
                people.append(employee)
                print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary:.1f}.")
            
            case '3':
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                department = input("Enter Department: ")
                manager = Manager(name, age, emp_id, salary, department)
                people.append(manager)
                print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.1f}, and department: {department}.")
            
            case '4':
                if not people:
                    print("\nNo records to display.")
                    continue
                
                print("\nChoose details to show:")
                print("1. Show all records")
                print("2. Show only Persons")
                print("3. Show only Employees")
                print("4. Show only Managers")
                
                show_choice = input("Enter your choice: ")
                
                print("\n--- Displaying Records ---")
                for i, person in enumerate(people, 1):
                    match show_choice:
                        case '1':
                            print(f"\nRecord {i}:")
                            person.display()
                        case '2':
                            if isinstance(person, Person) and not isinstance(person, Employee):
                                print(f"\nRecord {i} (Person):")
                                person.display()
                        case '3':
                            if isinstance(person, Employee) and not isinstance(person, Manager):
                                print(f"\nRecord {i} (Employee):")
                                person.display()
                        case '4':
                            if isinstance(person, Manager):
                                print(f"\nRecord {i} (Manager):")
                                person.display()
                        case _:
                            pass  # Invalid choice will be ignored
            
            case '5':
                print("\nExiting the system. All resources have been freed.")
                print("Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please try again.")


def demonstrate_oop_concepts():
    print("\n--- Demonstrating OOP Concepts ---")
    
    print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
    print(f"Is Employee a subclass of Person? {issubclass(Employee, Person)}")

    emp = Employee("Test", 25, "E999", 30000)
    print(f"\nEncapsulation demonstration:")
    print(f"Employee ID via getter: {emp.get_employee_id()}")
    emp.set_salary(35000)
    print(f"Updated salary via setter: ${emp.get_salary():.1f}")


if __name__ == "__main__":
    demonstrate_oop_concepts()
    main()