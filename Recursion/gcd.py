def gcd(a,b):  
      
    if (a == 0):  
        return b  
    elif (b == 0):  
        return a    
    elif (a == b):  
        return a    
    elif (a > b):  
        return gcd(a-b, b)   
    return gcd(a, b-a)  
a = int(input("Enter the numver 1 : "))
b = int(input("Enter the numver 2 : "))  
if(gcd(a, b)):  
    print('GCD of', a, 'and', b, 'is', gcd(a, b))  
else:  
    print('not found')  