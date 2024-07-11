"""
1. Heapify: Ensures the max heap property is maintained for the subtree rooted at a given index.

2. Build Max Heap: Transforms the input array into a max heap.

3. Heap Sort: Extracts the maximum element (root of the heap) and heapifies the remaining elements until the array is sorted.
"""

def heapify(arr, n, i):
    largest = i #Initializing the largest as root
    left = 2 * i + 1 # left = 2 * i + 1
    right = 2 * i + 2 # right = 2 * i + 2

    # If left child is larger than the root
    if(left < n and arr[left] > arr[largest]):
        largest = left
    
    # If right child is larger than the largest so far
    if(right < n and arr[right] > arr[largest]):
        largest = right
    
    # If largest is not root
    if(largest != i):
        arr[i], arr[largest] = arr[largest], arr[i] #Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def build_max_heap(arr):
    arr_length = len(arr)

    # Start from the last non-leaf node and heapify each node
    for i in range(arr_length // 2 -1, -1, -1):
        heapify(arr, arr_length, i)

def heap_sort(arr):
    n = len(arr)

    build_max_heap(arr)

    # Step 3.2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage:
numbers = [64, 25, 12, 22, 11]
heap_sort(numbers)
print("Sorted list:", numbers)