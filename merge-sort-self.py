def merge_sort(arr):
    if len(arr)<1:
        return arr
    
    mid = len(arr)//2
    left = merge(arr[0:mid])
    right = merge(arr[mid:])
    return merge(left,right)
    
def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
        else:
            result.append(right[j])
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
    