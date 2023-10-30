def factor(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i
n = int(input("Input a number: "))
factors = factor(n)
print("Factors of", n)
for i in factors:
    print(i, end = ", ")