def cube(n):
    for i in range(1,n+1):
        yield i**3
n = int(input("Enter the limit :"))
cubes = cube(n)
print("Cube of numbers from 1 to ",n)
for j in cubes:
    print(j)