# Initial unsorted list
numbers = [64, 34, 25, 12, 22, 90, 11]
print("Initial numbers in the list: ", numbers)
print("---------------------------------------")
listLength = len(numbers)

# Outer loop for each pass or number of elements in the list.
# Each pass will push the largest unsorted element to its correct position.
for i in range(listLength):
    swapped = False  # Flag to detect any swap
    # Inner loop for comparing and swapping
    # This code adds the inner loop that goes from the start of the list to n - i - 1 (since the last i elements are already sorted after each pass)
    for j in range(0, listLength - i - 1):
        # Compare adjacent elements
        if(numbers[j] > numbers[j + 1]):
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True  # Set the flag to True
    print(f"After pass {i+1}: {numbers}")
    # If no two elements were swapped, the list is sorted.
    if not swapped:
        break
print("---------------------------------------")
print("Sorted List: ", numbers)