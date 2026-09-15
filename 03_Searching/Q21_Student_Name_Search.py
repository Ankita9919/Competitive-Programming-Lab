students = input("Enter student names: ").split()

target = input("Enter name to search: ")

found = False

for i in range(len(students)):
    if students[i].lower() == target.lower():
        print("Student found at index:", i)
        found = True
        break

if not found:
    print("Student not found")
