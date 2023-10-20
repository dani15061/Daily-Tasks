def lcm(x, y):  
    z = x % y  
    if z == 0:  
        return x  
    return x * lcm(y, z) / z  
x = int(input("Enter the numver 1 : "))
y = int(input("Enter the numver 2 : "))
print("The least common factor is: ", lcm(x, y))  