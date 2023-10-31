#sorting matrix
n1 = int(input("Enter the number of rows :"))
n2 = int(input("Enter the number of columns :"))
m = []
for i in range(n1):
    s = []
    for j in range(n2):
        s.append(int(input()))
    m.append(s)
for i in range(n1):
    for j in range(n2):
        print(m[i][j], end = " ")
    print()
n = len(m)
x = []
for i in range(n):
    for j in range(n):
        x.append(m[i][j])
x.sort()
k = 0
for i in range(n):
    for j in range(n):
        m[i][j] = x[k]
        k += 1
print("Sorted Matrix will be: ")
for i in range(n):
    for j in range(n):
        print(m[i][j], end=" ")
    print("")