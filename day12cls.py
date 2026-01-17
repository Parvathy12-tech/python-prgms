def mini_library():
    try:
        title = input("Enter book title: ")
        year = input("Enter publication year: ")

        if not all(ch.isalpha() or ch.isspace() for ch in title):
            raise ValueError("Error: Book title must contain only alphabets and spaces.")

        if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
            raise ValueError("Error: Publication year must be a 4-digit number starting with '19' or '20'.")

        print(f"Book accepted: '{title}' published in {year}")

    except ValueError as e:
        print(e)

    finally:
        print("Program finished. Thank you for using the mini library system.")


mini_library()