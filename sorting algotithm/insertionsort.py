def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j] :
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
insertionSort(a)
for i in range(len(a)):
    print("% d" % a[i] ,end="  ")