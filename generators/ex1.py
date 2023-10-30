'''
#generator
def gen():
    yield 15
    yield 6
    yield 2001
for i in gen():
    print(i)
#generator as iterator
def gen1():
    yield 15
    yield 6
    yield 2001
x = gen1()
print(next(x))
print(next(x))
print(next(x))
#fibbonacci
def fib(limit):
    a,b = 0,1
    while a< limit:
        yield a
        a,b = b,a+b
n = int(input("Enter the limit : "))
x = fib(n)
print("loop")
for i in fib(n):
    print(i)
#generator expression
genexp = (i*5 for i in range(10) if i%2 == 0)
for i in genexp:
    print(i)
'''
