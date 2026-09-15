import re

code = input("Enter book code: ")

if re.fullmatch(r"LIB-\d{4}", code):
    print("Valid Book Code")
else:
    print("Invalid Book Code")
