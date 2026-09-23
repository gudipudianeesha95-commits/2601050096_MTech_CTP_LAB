import sys

# List
numbers = [x * 2 for x in range(10000)]

# Generator
generator = (x * 2 for x in range(10000))

print("List Memory:", sys.getsizeof(numbers))
print("Generator Memory:", sys.getsizeof(generator))