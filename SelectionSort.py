# Initial unsorted list
numbers = [64, 25, 12, 22, 11]
print("Initial list:", numbers)
print("---------------------------------------")

listLength = len(numbers) # Get the length of the list

# Outer loop to move the boundary of the unsorted sublist.
# We need to create an outer loop that will iterate through the list and find the minimum element from the unsorted part of the list in each pass
#Outer Loop: Moves the boundary of the unsorted sublist.
for i in range(listLength):
    # Find the minimum element in the remaining unsorted list
    min_index = i
    # Inner Loop: Finds the minimum element in the remaining unsorted list.
    for j in range(i + 1, listLength):
        if(numbers[j] < numbers[min_index]):
            min_index = j
    # Swap the found minimum element with the first element of the unsorted list
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    print(f"After pass {i+1}: {numbers}")
print("---------------------------------------")
print("Sorted List: ", numbers)