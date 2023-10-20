def ternary(l, r, key, a):
    if (r >= l):
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
        if (a[mid1] == key): 
            return mid1
        if (a[mid2] == key): 
            return mid2
        if (key < a[mid1]): 
            return ternary(l, mid1 - 1, key, a)
        elif (key > a[mid2]): 
            return ternary(mid2 + 1, r, key, a)
        else: 
            return ternary(mid1 + 1, 
                                 mid2 - 1, key, a)
    return -1

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
l = 0
r = len(a)-1
key =  int(input("Enter the element to be searched : "))
p = ternary(l, r, key, a)
print("Index of", key, "is", p)
