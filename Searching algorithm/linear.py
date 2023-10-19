def search(a, N, x): 
    for i in range(0, N): 
        if (a[i] == x): 
            return i 
    return -1
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
x = 10
N = len(a)   
result = search(a, N, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result) 