import heapq

patients = []

n = int(input("Enter number of patients: "))

for _ in range(n):
    name = input("Enter patient name: ")
    severity = int(input("Enter severity: "))

    heapq.heappush(patients, (-severity, name))

print("Emergency Order:")

while patients:
    severity, name = heapq.heappop(patients)

    print(name, "- Severity:", -severity)
