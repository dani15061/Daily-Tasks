'''
#print list
l = [ch for ch in [1,2,3]]
print(l)
#Print even numbers
l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
l = [ch for ch in l1 if ch%2 == 0]
print(l)
#matrix
m = [[j for j in range(8) if j%2 == 1]for i in range(8) if i%2 == 0]
print(m)
l = [ch for ch in 'Geeks 4 Geeks']
print(l)
n = [i*10 for i in range(1,7)]
print(n)
#square
l = [n**2 for n in range(1,10)]
print(l)
#matrix tranpose
m = [[10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]]
t = [[i[j] for i in m]for j in range(len(m[0]))]
print(t)
#reverse string
l = [i[::-1] for i in ('dharani','shree','dani')]
print(l)
'''
