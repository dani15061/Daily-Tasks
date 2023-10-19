def bubblesort(a):
    k = len(a)
    for i in range(k):
        swapped = False
        for j in range(0,k-i-1):
            if a[j] >a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if(swapped == False):
            break

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
bubblesort(a)
print("The sorted array : ")
for i in range(len(a)):
    print("%d" %a[i],end = "  ")