def sentinelSearch(a, N, key):
    last = a[N - 1]
    a[N - 1] = key
    i = 0
    while (a[i] != key):
        i += 1
    a[N - 1] = last
 
    if ((i < N - 1) or (a[N - 1] == key)):
        print(key, "is present at index", i)
    else:
        print("Element Not found")
 
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
N = len(a)
key = int(input("Enter the element to be searched : "))
 
sentinelSearch(a, n, key)