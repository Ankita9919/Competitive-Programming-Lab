base = int(input("Enter base address: "))
lower_bound = int(input("Enter lower bound: "))
index = int(input("Enter element index: "))
word_size = int(input("Enter word size in bytes: "))

effective_address = base + (index - lower_bound) * word_size

print("Effective Address:", effective_address)
