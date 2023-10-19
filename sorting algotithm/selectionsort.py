a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The list is ",a)
for i in range (len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[min] > a[j]:
            min = j
    a[i],a[min] = a[min],a[i]
print("Sorted array : ")
for i in range(len(a)):
    print("%d" %a[i],end = "  ")
