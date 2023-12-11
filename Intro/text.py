import random
l = ['fruits', 'animals','food']
d = {'fruits' :['strawberry','apple','mango','orange','banana','pineapple'], 'animals':['lion','tiger','dog','cat','horse'],'food':['Salad','Sandwich','Bread','Steak','Fish','shrimp','Rice']
}
l1 = random.choice(l)
print(l1)
if l1 in d:
    d1 = d[l1][random.randint(0,len(d[l1]) -1)]
    print(d1)
