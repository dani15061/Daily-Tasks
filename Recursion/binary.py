def binarySearch (a, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if a[mid] == x: 
            return mid 
        elif a[mid] > x: 
            return binarySearch(a, l, mid-1, x) 
        else: 
            return binarySearch(a, mid+1, r, x) 
    else:
        return -1

a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
x = int(input("Enter the element to be searched : "))
k = binarySearch(a,0,len(a)-1,x)
if(k!=-1):
  print('Found at position :',k+1)
else:
  print('Not found')