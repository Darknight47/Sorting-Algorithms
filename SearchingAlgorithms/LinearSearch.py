def linear_search(arr, target):
    """
        Perform a linear search on the given list.

        Parameters:
        arr (list): The list to search through.
        target (any): The target value to search for.

        Returns:
        int: The index of the target value if found, otherwise -1.
    """
    # Iterate through each element in the list
    for i in range(len(arr)):
        # Check if the current element is the target
        if(arr[i] == target):
            return i
    # Target not found in the list, return -1
    return -1

arr = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(arr, target)

if(result != -1):
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")