# partition function rearranges the elements in the array so that all elements less than the pivot come before it and all elements greater come after it.
def partition(arr, low, high):
    pivot = arr[high] # chooses the last element as the pivot.
    i = low - 1 # Pointer for the smallest element. We initialize i to be one less than the low index. This is because we will increment i before swapping any elements.

    for j in range(low, high):
        if(arr[j] <= pivot): # If current element is smaller than or equal to the pivot.
            i += 1 # Increment the pointer.
            arr[i], arr[j] = arr[j], arr[i] # Swap the elements.
            # This ensures that all elements less than or equal to the pivot are on the left side of the pivot.
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap the pivot element with the element at i+1
    # This places the pivot between the two partitions: elements less than or equal to the pivot are on the left, and elements greater than the pivot are on the right.
    print("Swapped: ", arr)
    print("--------------------------------")
    return i + 1 # Return the partition index 
# Example usage of partition function:
# numbers = [64, 25, 12, 22, 11]
# pi = partition(numbers, 0, len(numbers) - 1)
# print("Partitioned list:", numbers)
# print("Partition index:", pi)

def quick_sort(arr, low, high):
    if(low < high):
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1) # This call sorts the sub-array that contains elements before the pivot.
        print("Sorted before partition: ", arr)
        print("--------------------------------")
        quick_sort(arr, pi + 1, high) # This call sorts the sub-array that contains elements after the pivot.
        print("Sorted after partition: ", arr)
        print("--------------------------------")

# Example usage of quick_sort:
numbers = [64, 25, 12, 22, 11]
print("Initial list: ", numbers)
quick_sort(numbers, 0, len(numbers) - 1)
print("Sorted list:", numbers)