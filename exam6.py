import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename
    
    def get_current_datetime(self):
        return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    
    def add_entry(self):
        try:
            entry = input("Enter your journal entry:\n")
            current_datetime = self.get_current_datetime()
            
            with open(self.filename, 'a') as file:
                file.write(f"{current_datetime}\n{entry}\n\n")
            
            print(f"\nEntry added successfully at {current_datetime}!")
        
        except PermissionError:
            print("Error: Permission denied. Cannot write to file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def view_all_entries(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            
            if content.strip():
                print("\nYour Journal Entries:")
                print("=" * 50)
                print(content)
                print("\nNote: All timestamps show when each entry was created.")
            else:
                print("\nNo journal entries found. Start by adding a new entry!")
        
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def search_entry(self):
        try:
            keyword = input("Enter a keyword to search in journal entries: ").lower()
            
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            
            matching_entries = []
            current_entry = ""
            current_timestamp = ""
            in_entry = False
            
            for line in lines:
                line_stripped = line.strip()
                
                if line.startswith('['): 
                    current_timestamp = line_stripped
                    current_entry = ""
                    in_entry = True
                elif in_entry and line_stripped:
                    current_entry += line
                elif not line_stripped:  
                    if current_entry and keyword in current_entry.lower():
                        matching_entries.append((current_timestamp, current_entry.strip()))
                    current_timestamp = ""
                    current_entry = ""
                    in_entry = False
            
            if current_entry and keyword in current_entry.lower():
                matching_entries.append((current_timestamp, current_entry.strip()))
            
            if matching_entries:
                print(f"\nFound {len(matching_entries)} matching entries:")
                print("=" * 50)
                for timestamp, entry in matching_entries:
                    print(f"{timestamp}")
                    print(f"{entry}")
                    print()  
            else:
                print(f"\nNo entries were found containing: '{keyword}'")
        
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def delete_all_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return
            
            confirmation = input("Are you sure you want to delete all entries? (yes/no): ").lower()
            
            if confirmation == 'yes':
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            else:
                print("\nDeletion cancelled.")
        
        except PermissionError:
            print("Error: Permission denied. Cannot delete the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def display_menu(self):
        print("\n" + "="*50)
        print("Welcome to Personal Journal Manager!")
        print("="*50)
        print("Please select an option:")
        print("1. Add a New Entry (with current date/time)")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
    
    def run(self):
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-5): ")
                
                if choice == '1':
                    self.add_entry()
                elif choice == '2':
                    self.view_all_entries()
                elif choice == '3':
                    self.search_entry()
                elif choice == '4':
                    self.delete_all_entries()
                elif choice == '5':
                    print("\nThank you for using Personal Journal Manager. Goodbye!")
                    break
                else:
                    print("\nInvalid option. Please select a valid option from the menu.")
            
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")

journal = JournalManager()
journal.run()