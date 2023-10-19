def shellSort(a, n): 
    gap=n//2  
    while gap>0: 
        j=gap 
        while j<n: 
            i=j-gap    
            while i>=0: 
                if a[i+gap]>a[i]: 
                    break
                else: 
                    a[i+gap],a[i]=a[i],a[i+gap] 
                i=i-gap  
            j+=1
        gap=gap//2
  
  
  
  
  
a = []
n = int(input("Enter the length of the list : "))
for k in range(0 , n):
    l = int(input())
    a.append(l)
print("The array is",a)
  
shellSort(a,len(a)) 
print("sorted array",a)