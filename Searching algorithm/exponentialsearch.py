def binarySearch( a, l, r, x):
    if r >= l:
        mid = l + ( r-l ) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearch(a, l,  mid - 1, x)
        return binarySearch(a, mid + 1, r, x)
    return -1
def exponentialSearch(a, N, x):
    if a[0] == x:
        return 0
    i = 1
    while i < N and a[i] <= x:
        i = i * 2
    return binarySearch( a, i // 2,  min(i, N-1), x)
     

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
N = len(a)
x = int(input("Enter the element to be searched : "))
result = exponentialSearch(a, N, x)
if result == -1:
    print ("Element not found in the array")
else:
    print ("Element is present at index %d" %(result))
 