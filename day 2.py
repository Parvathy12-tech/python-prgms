header = """\n\tBOOKSTORE RECEIPT
\t-----------------\n"""

book1 = "Book Title: {} \t Price: ₹{}"
book2 = "Book Title: {} \t Price: ₹{}"

line1 = book1.format("Python Basics", 450)
line2 = book2.format("Data Science Intro", 600)

total_price = 450 + 600
total_line = "TOTAL \t\t\t ₹{}".format(total_price)

receipt = header + line1 + "\n" + line2 + "\n" + total_line + "\n\n\tTHANK YOU FOR SHOPPING WITH US!"

print(receipt.upper())