def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
def printList(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("Given array is")
printList(a)
mergeSort(a)
print("\nSorted array is ")
printList(a)