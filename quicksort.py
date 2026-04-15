def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1,len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [10,5,6,5,8,84,1,9]
sorted_array = quick_sort(arr)
print(sorted_array)
