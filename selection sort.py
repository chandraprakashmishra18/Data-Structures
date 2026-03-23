# def selectionsort(arr):
#     n = len(arr)
    
#     for i in range (n):
#         min_idx = i
        
#         for j in range (i+1,n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
                
#         arr[i],arr[min_idx] = arr[min_idx],arr[i]
        
#     return arr

# arr1 = [4,5,3,6,9,1,2]
# print(selectionsort(arr1))
                
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr1 = [4,5,3,6,9,1,2]
print(selection_sort(arr1))