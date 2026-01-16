paragraph = """  
Python is a popular programming language.  
This Python course introduces basics and helps beginners learn step by step.  
"""

print("Length of paragraph:", len(paragraph))
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview (first 50 chars):", paragraph[:50])

updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python':\n", updated_paragraph)

lower_paragraph = paragraph.lower()
print("\nLowercase version:\n", lower_paragraph)

trimmed_paragraph = paragraph.strip()
print("\nTrimmed paragraph:\n", trimmed_paragraph)

words = trimmed_paragraph.split()
print("\nList of words:\n", words)

if "course" in trimmed_paragraph.lower():
    print("\nThe word 'course' was found in the paragraph.")

final_message = "The course description is {} characters long and has {} words.".format(
    len(trimmed_paragraph), len(words)
)
print("\n" + final_message)