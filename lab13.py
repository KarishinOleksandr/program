add_ten = lambda a: a + 10

result = add_ten(5)
print(result)  

three = lambda x, y, z: x * y * z

result = three(2, 3, 4)
print(result)  

a = lambda: 2
b = lambda x: 1 if x > 3 else 1
c = lambda x: x
d = lambda x, y: x + y
e = lambda x, y: y if x > 1 else y
f = lambda x, y: int(str(x) + str(y))
g = lambda x: lambda y: int(str(x) + str(y))
h = lambda x=None: (lambda y: 5 if y is None else 5 + y)
i = lambda x, y: lambda z: (x if z == 2 else y) if z == 2 else (y if z == 5 else x)
j = lambda x: lambda z: x(2)
k = lambda x: lambda y: x(y())
m = lambda x: x + 2
n = lambda: 3
o = lambda x: x
p = lambda x, y: lambda z: str(y(z)) + ' ' + str(x(z))
q = lambda x: lambda y: y() + ' ' + x
r = lambda x, y: x + y() // 1000
s = lambda x: lambda y: y + ' ' + x
def t(x):
    return lambda y: 'arctan'
def u(x):
    return 'arccosine'
def v():
    return 'arccosecant'

print(a())  
print(b(3))  
print(b(10))  
print(b(2))  
print(c(1))  
print(c(3))  
print(d(1, 3))  
print(d(2, 5))  
print(e(1, 3))  
print(e(2, 5))  
print(f(2, 5))  
print(f(3, 1))  
print(g(1)(2))  
print(g(2)(1))  
print(h()(2))  
print(h()(3))  
print(i(2, 5)(2))  
print(i(3, 5)(2))  
print(j(lambda x: x(2)))  
print((lambda x: x(2))(k))  
print((lambda x: lambda y: x(y()))(m)(n))  
print(o('cal')) 
print(p(lambda x: x + 2, lambda x: x + 3)(1)) 
print(q('veggies')(lambda: 'eat'))  
new_year = (lambda x: lambda: x)(2000)
happy = r(30, lambda: new_year() // 1000)
print(happy)  
print(s(lambda x: x()('cal'))) 
print(t('ta')('n')) 
print(u('sine'))  
print(v()) 

a = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
ado2 = list(map(lambda x: x**2, a))
print(ado2)

from functools import reduce

a = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
mnozh = reduce(lambda x, y: x * y, a)
print(mnozh)

lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

sorrt = sorted(lst, key=lambda x: x[1][-1], reverse=True)
print(sorrt)
