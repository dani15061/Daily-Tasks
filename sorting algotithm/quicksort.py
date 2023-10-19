def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            (a[i], a[j]) = (a[j], a[i])
    (a[i + 1], a[high]) = (a[high], a[i + 1])
    return i + 1
def quicksort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi - 1)
 
        quicksort(a, pi + 1, high)

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
N = len(a)
quicksort(a, 0, N - 1)
print('Sorted array:')
for x in a:
    print(x, end=" ")