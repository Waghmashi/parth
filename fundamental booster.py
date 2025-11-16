# Simple Personal Data Collector

print("Welcome to Personal Data Collector!")
print("Please enter your details:")

# Collect information
name = input("Your name: ")
age = int(input("Your age: "))
height = float(input("Your height (meters): "))
fav_number = int(input("Your favorite number: "))

# Calculate birth year
birth_year = 2025 - age

print("\n--- Your Information ---")
print(f"Name: {name} (Type: {type(name)}, ID: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, ID: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, ID: {id(height)})")
print(f"Favorite Number: {fav_number} (Type: {type(fav_number)}, ID: {id(fav_number)})")

print(f"\nYour birth year is approximately: {birth_year}")

print("\nThank you for using our program!")