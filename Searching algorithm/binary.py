def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
 
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
  
x = 10
 
   
result = binarySearch(a, 0, len(a)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")