frontend_students = {"Alice", "Bob", "Charlie", "Diana"}
backend_students = {"Charlie", "Eve", "Frank"}


backend_students.add("Grace")

frontend_students.remove("Bob")


both_courses = frontend_students & backend_students
print("Students enrolled in both courses:", both_courses)

backend_only = backend_students - frontend_students
print("Students only in Backend:", backend_only)


total_unique_students = frontend_students | backend_students
print("Total unique students:", len(total_unique_students))


course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}


for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")


updated_courses = {
    course: (course_counts["Frontend"] + course_counts["Backend"]
             if course == "Fullstack" else course_counts[course])
    for course in ["Frontend", "Backend", "Fullstack"]
}

print("Updated course dictionary:", updated_courses)