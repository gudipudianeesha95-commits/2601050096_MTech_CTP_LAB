def merge_sort(arr):

    # If list has one or zero elements
    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide the list
    left = arr[:mid]
    right = arr[mid:]

    # Sort both parts
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge both sorted parts
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare elements
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original List:", numbers)

# Apply Merge Sort
sorted_numbers = merge_sort(numbers)

print("Sorted List:", sorted_numbers)