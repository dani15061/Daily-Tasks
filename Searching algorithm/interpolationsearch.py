def interpolationSearch(a, l, h, x):
    if (l <= h and x >= a[l] and x <= a[h]):
        pos = l + ((h - l) // (a[h] - a[l]) *(x - a[l]))
        if a[pos] == x:
            return pos
        if a[pos] < x:
            return interpolationSearch(a, pos + 1, h, x)
        if a[pos] > x: 
            return interpolationSearch(a, l, pos - 1, x)
    return -1
 
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
N = len(a)
x = int(input("Enter the element to be searched : "))
ind = interpolationSearch(a, 0, N - 1, x)
if ind != -1:
    print("Element found at index", ind)
else:
    print("Element not found")
 