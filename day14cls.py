import random
import math

names_input = input("Enter guest names (comma-separated): ")
names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))
chosen_name = random.choice(unique_names)
reversed_name = chosen_name[::-1]
count_unique = len(unique_names)
sqrt_rounded = round(math.sqrt(count_unique))

print("\n--- Birthday Name Game ---")
print(f"Unique guest names: {unique_names}")
print(f"Total unique names: {count_unique}")
print(f"Rounded square root of total: {sqrt_rounded}")
print(f"Chosen name: {chosen_name}")
print(f"Reversed chosen name: {reversed_name}")