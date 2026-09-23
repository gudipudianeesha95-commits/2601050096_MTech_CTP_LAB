**EXPERIMENT 1 — Merge Sort**

**Aim**

To implement Merge Sort using Divide and Conquer.

**Algorithm**

Divide the list into two halves.
Sort both halves.
Merge the sorted halves.
Display the sorted list.
Python Program
def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


a = [38, 27, 43, 3, 9]

print("Original:", a)
print("Sorted:", merge_sort(a))
Output
Original: [38, 27, 43, 3, 9]
Sorted: [3, 9, 27, 38, 43] 

**Data & Result**

Input: [38,27,43,3,9]
Output: [3,9,27,38,43]

**Inference & Analysis**

Merge Sort successfully sorted the data.

Time Complexity: O(n log n)

**Result**

Thus, Merge Sort was successfully implemented.
