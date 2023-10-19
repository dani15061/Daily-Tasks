def heapify(a, N, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2    
    if l < N and a[largest] < a[l]:
        largest = l
    if r < N and a[largest] < a[r]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]  
        heapify(a, N, largest) 
def heapSort(a):
    N = len(a)
    for i in range(N//2 - 1, -1, -1):
        heapify(a, N, i)
    for i in range(N-1, 0, -1):
        a[i], a[0] = a[0], a[i] 
        heapify(a, i, 0)

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
heapSort(a)
N = len(a)
 
print("Sorted array is")
for i in range(N):
    print("%d" % a[i], end=" ")