# Initial unsorted list
numbers = [64, 25, 12, 22, 11]
print("Initial list:", numbers)
print("---------------------------------------")

listLength = len(numbers) # Get the length of the list

# Outer loop to iterate through each element
# The outer loop starts from the second element and runs through the entire list.
for i in range(listLength):
    key = numbers[i] # Element to be inserted
    j = i - 1

    # Move elements of numbers[0..i-1], that are greater than key, to one position ahead of their current position
    # Moves elements that are greater than the key to one position ahead.
    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    
    numbers[j + 1] = key  # Insert the key element at the correct position

    # Print the current state of the list
    print(f"Pass {i}: {numbers}")
print("---------------------------------------")
print("Sorted list:", numbers)