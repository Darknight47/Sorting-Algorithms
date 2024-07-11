def bucket_sort(arr):
    arrayLength = len(arr)
    if(arrayLength <= 0):
        return arr
    
    # Create n empty buckets
    buckets = [[] for _ in range(arrayLength)]

    # Distribute the elements into the appropriate buckets
    for num in arr:
        index = int(num * arrayLength) #Index in bucket
        buckets[index].append(num)
    
    # Sort each bucket
    for b in range(arrayLength):
        buckets[b] = sorted(buckets[b])
        
    # Concatenate the sorted buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array
numbers = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_numbers = bucket_sort(numbers)
print("Sorted list:", sorted_numbers)