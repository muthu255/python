import sys
import gc
print('============')
a=10
b=10

print(id(a))

print(id(b))

print('a is b', a is b)
print('a==b',a==b)

print('============')
a=500
print(id(a))
b=500
print(id(b))


print('a is b', a is b)

print('a==b',a==b)

print('============')

a=[1,2,3]
b=[1,2,3]


print(id(a))

print(id(b))
print('a is b', a is b)

print('a==b',a==b)

print('============')

