**EXPERIMENT 4 — List vs Generator**

The workbook asks to compare list-based and generator-based processing for a large dataset in terms of execution time and memory usage.

**Aim**

To compare List and Generator processing.

**Algorithm**

1. Create a large dataset.

2. Process it using a list.

3. Process it using a generator.

4. Compare memory and execution time.

**Python Program**
import sys

*# List
numbers = [x * 2 for x in range(10000)]

*# Generator
generator = (x * 2 for x in range(10000))

print("List Memory:", sys.getsizeof(numbers))
print("Generator Memory:", sys.getsizeof(generator))

**Output**

Example:

List Memory: 85176
Generator Memory: 200

**Data & Result**

The list uses more memory.

The generator uses less memory.

**Inference & Analysis**

Generators produce values one at a time, so they generally use less memory.

**Result**

Thus, generator-based processing is memory efficient for large datasets.
