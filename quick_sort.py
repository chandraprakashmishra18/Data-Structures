def quick_sort(arr , low , high):
    if high>low:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
        
def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if pivot > arr[j]:
            i += 1
            arr[j],arr[i] = arr[i] , arr[j]
            
    arr[high] , arr[i+1] = arr[i+1] , arr[high]
    return i+1

arr = [4, 2, 7, 1, 3]
quick_sort(arr, 0, len(arr)-1)

print(arr) 