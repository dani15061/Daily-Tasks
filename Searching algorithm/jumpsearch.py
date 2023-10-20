import math
def jumpSearch( a , x , n ):
    step = math.sqrt(n)
    prev = 0
    while a[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while a[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if a[int(prev)] == x:
        return prev
    return -1
 
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
x = int(input("Enter the element to be searched : "))
n = len(a)
index = jumpSearch(a, x, n)
print("Number" , x, "is at index" ,"%.0f"%index)
