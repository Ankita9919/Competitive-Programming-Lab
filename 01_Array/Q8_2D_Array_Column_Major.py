# Column Major Formula:
# EA = Base + (Column * Rows + Row) * Element Size

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
base = int(input("Enter base address: "))
size = int(input("Enter element size: "))
i = int(input("Enter row index: "))
j = int(input("Enter column index: "))

address = base + (j * rows + i) * size

print("Effective Address:", address)
