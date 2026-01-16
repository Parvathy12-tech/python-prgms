item = input("Enter the name of the new stationery item: ")

with open("items.txt", "a") as file:
    file.write(item + "\n")

print("\nCurrent list of items:")
with open("items.txt", "r") as file:
    items = file.readlines()
    for i, line in enumerate(items, start=1):
        print(f"{i}. {line.strip()}")