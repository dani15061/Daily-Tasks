def permutations(a):
    if len(a) <= 1:
        yield a
    else:
        for p in permutations(a[1:]):
            for i in range(len(a)):
                yield p[:i] + a[0:1] + p[i:]
l = []
n = int(input("Enter the length of list : "))
for k in range(n):
    s = int(input())
    l.append(s)
print("Original list of elements:",l)

print("All permutations:")
for p in permutations(l):
    print(p)