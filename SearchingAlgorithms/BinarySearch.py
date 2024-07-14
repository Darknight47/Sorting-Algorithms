def binary_search(arr, target):
    """
        Perform a binary search on the given sorted list.
        Parameters:
        arr (list): The sorted list to search through.
        target (any): The target value to search for.

        Returns:
        int: The index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while(left <= right):
        middle = (left + right) // 2

        # Checking if the middle element is the target
        if(arr[middle] == target):
            return middle
        # If target is less than the middle element, adjust the right pointer
        elif(arr[middle] > target):
            right = middle - 1
        # If target is greater than the middle element, adjust the left pointer
        else:
            left = middle + 1
    # Target not found in the list
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")