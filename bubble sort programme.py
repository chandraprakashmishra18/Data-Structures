def bubblesort(arr):
    n = len(arr)
    for i in range(n):
     swapped = False
     for j in range( 0 , n-i-1 ):
        if arr[j]>arr[j+1]:
         arr[j],arr[j+1] = arr[j+1],arr[j]
         swapped = True
     if not swapped:
         break
    return arr
     
arr1 = [4,5,3,6,9,1,2]
print(bubblesort(arr1))