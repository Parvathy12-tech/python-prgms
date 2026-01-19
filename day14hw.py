import random
import math

names_input = input("Enter customer names (comma-separated): ")
names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))

random.shuffle(unique_names)
winners = random.sample(unique_names, 2)

reversed_winners = [winner[::-1] for winner in winners]
count_unique = len(unique_names)
sqrt_rounded = round(math.sqrt(count_unique))

print("\n--- Lucky Draw Results ---")
print(f"Unique participants: {unique_names}")
print(f"Total unique participants: {count_unique}")
print(f"Rounded square root of participants: {sqrt_rounded}")
print(f"Winners: {winners}")
print(f"Reversed winners: {reversed_winners}")