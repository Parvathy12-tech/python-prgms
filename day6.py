attendance = [18, 20, 19, 15, 21]

# Task 1: Loop through and check if class was full
full_days = 0
total_attendance = 0

for students in attendance:
    if students >= 20:
        print("Full")
        full_days += 1
    else:
        print("Not Full")
    total_attendance += students

# Task 2: Count how many days the class was full
print("Number of full days:", full_days)

# Task 3: Calculate total attendance
print("Total attendance over 5 days:", total_attendance)