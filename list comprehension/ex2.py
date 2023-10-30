#if else in list comprehensions
#odd or even
'''
l = ["even num" if i%2 == 0 else "odd num"for i in range(10)]
print(l)
l1 = [n for n in range(200) if n%5 == 0 if n%10 == 0]
print(l1)
names = ["G", "G", "g"]
ages = [25, 30, 35]
t =[(name ,age) for name , age in zip(names , ages)]
print(t)
'''
def digit(n):
    sum = 0
    for j in str(n):
        sum += int(j)
    return sum
l = []
n = int(input("Enter the length of list : "))
for k in range(n):
    s = int(input())
    l.append(s)
print(l)

l1 = [digit(i) for i in l]
print(l1)
