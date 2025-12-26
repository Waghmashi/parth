import os
from datetime import datetime

class FileHandler:
    def check_file(self, filename):
        return os.path.isfile(filename)
    
    def remove_file(self, filename):
        os.remove(filename)
  
class TimeHandler:
    def get_time_now(self):
        return datetime.now()

class SimpleJournal(FileHandler, TimeHandler):
    def __init__(self):
        self.filename = "my_journal.txt"
    
    def add(self):
        print("\n--- Add New Entry ---")
        text = input("Enter your journel entry?\n")
        
        now = self.get_time_now()
        date_str = now.strftime("[%d-%m-%Y %I:%M %p]")
        
        try:
            with open(self.filename, "a") as f:
                f.write(f"{date_str}\n")
                f.write(f"{text}\n")
                f.write("-" * 40 + "\n\n")
            
            print(f"\nSaved! Time: {date_str}")
        
        except:
            print("Could not save. Try again.")
    
    def view(self):
        print("\n--- View all entry ---")
        
        if not self.check_file(self.filename):
            print("No entries yet!")
            return
        
        try:
            with open(self.filename, "r") as f:
                all_text = f.read()
            
            if all_text:
                print(all_text)
            else:
                print("Journal is empty!")
        
        except:
            print("Could not read file.")
    
    def search(self):
        print("\n--- Search ---")
        
        if not self.check_file(self.filename):
            print("No entries to search!")
            return
        
        word = input("Enter a keyword or date to search: ").lower()
        
        try:
            with open(self.filename, "r") as f:
                entries = f.read().split("\n\n")
            
            found = []
            
            for entry in entries:
                if entry and word in entry.lower():
                    found.append(entry)
            
            if found:
                print(f"\nFound {len(found)} entries:")
                print("=" * 50)
                for entry in found:
                    print(entry)
                    print()
            else:
                print(f"\nNothing found with '{word}'")
        
        except:
            print("Search failed.")
    
    def delete_all(self):
        print("\n--- Delete All ---")
        
        if not self.check_file(self.filename):
            print("Already empty!")
            return
        
        answer = input("Delete ALL entries? (y/n): ").lower()
        
        if answer == 'y':
            try:
                self.remove_file(self.filename)
                print("All entries deleted!")
            except:
                print("Could not delete.")
        else:
            print("Not deleted.")
    
    def menu(self):
        print("\n" + "=" * 30)
        print("Please select an option")
        print("=" * 30)
        print("1. Add a new entry")
        print("2. View all entries")  
        print("3. Search entries")
        print("4. Delete all entries")
        print("5. Exit")
    
    def start(self):
        print("Welcome to Personal Journal Manager!")
        
        while True:
            self.menu()
            
            choice = input("\nYour choice (1-5): ")
            
            if choice == '1':
                self.add()
            elif choice == '2':
                self.view()
            elif choice == '3':
                self.search()
            elif choice == '4':
                self.delete_all()
            elif choice == '5':
                print("\nThank you for using Personal Journal Manager. Goodbye!!")
                break
            else:
                print("Please choose 1 to 5")

if __name__ == "__main__":
    journal = SimpleJournal()
    journal.start()