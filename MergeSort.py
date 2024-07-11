def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sorted lists into result-list.
    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    print("sorted: ", result)
    print("--------------------------")
    return result
# Example usage of merge function:
#left = [1, 3, 5]
#right = [2, 4, 6]
#print("Merged list:", merge(left, right))

# merge_sort function that will recursively split the list and use the merge function to combine the sorted sublists.
def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    # Divide: split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    print("left_half", left_half)
    print("right_half", right_half)
    print("--------------------------")

    # Conquer: recursively sort each half
    sorted_left = merge_sort(left_half) 
    sorted_right = merge_sort(right_half)   

    # Combine: merge the sorted halves.
    return merge(sorted_left, sorted_right)

# Example usage of merge_sort function.
numbers = [64, 25, 12, 22, 11]
print("Sorted list:", merge_sort(numbers))
