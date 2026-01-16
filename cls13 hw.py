import os
n = int(input("How many student names do you want to add? "))

new_names = []
for i in range(n):
    name = input(f"Enter name {i+1}: ")
    new_names.append(name)

filename = "students.txt"
if os.path.exists(filename):
    print("\nExisting names in the file:")
    with open(filename, "r") as file:
        existing_names = file.readlines()
        for line in existing_names:
            print(line.strip())
else:
    print("\nNo existing file found. Creating a new one...")

with open(filename, "a") as file:
    for name in new_names:
        file.write(name + "\n")

print("\nUpdated list of student names:")
with open(filename, "r") as file:
    updated_names = file.readlines()
    for line in updated_names:
        print(line.strip())