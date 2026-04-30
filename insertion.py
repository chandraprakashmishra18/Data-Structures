def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1 
        
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
arr = [4, 2, 7, 1, 3]
insertion_sort(arr)

print(arr) 