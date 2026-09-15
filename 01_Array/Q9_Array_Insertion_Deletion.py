arr = list(map(int, input("Enter array elements: ").split()))

print("Original Array:", arr)

pos = int(input("Enter position for insertion: "))
value = int(input("Enter value: "))

arr.insert(pos, value)

print("After Insertion:", arr)

pos = int(input("Enter position for deletion: "))

if 0 <= pos < len(arr):
    arr.pop(pos)
    print("After Deletion:", arr)
else:
    print("Invalid position")
