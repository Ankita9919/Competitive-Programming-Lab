n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    total = int(input("Enter total classes: "))
    attended = int(input("Enter attended classes: "))

    percentage = (attended / total) * 100

    print(name, "-", round(percentage, 2), "%")

    if percentage >= 75:
        print("Eligible")
    else:
        print("Short Attendance")
