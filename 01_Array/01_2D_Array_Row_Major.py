rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

base = int(input("Enter base address: "))
word_size = int(input("Enter word size in bytes: "))

i = int(input("Enter row index: "))
j = int(input("Enter column index: "))

offset = (i * cols + j) * word_size
effective_address = base + offset

print("Effective Address:", effective_address)
print("Binary Address:", bin(effective_address))
