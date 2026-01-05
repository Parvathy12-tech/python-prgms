python_students = {"Alice", "Bob", "Charlie"}
data_science_students = {"Bob", "Diana", "Eve"}

python_students.add("Frank")


data_science_students.remove("Eve")

both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)


python_only = python_students.difference(data_science_students)
print("Students only in Python:", python_only)

all_students = python_students.union(data_science_students)
print("All students (no duplicates):", all_students)

course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")


growth_projection = {course: count * 2 for course, count in course_counts.items()}
print("Expected growth (doubled counts):", growth_projection)