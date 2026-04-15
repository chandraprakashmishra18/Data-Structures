def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    return merge(left_arr,right_arr)

def merge(left_arr,right_arr)