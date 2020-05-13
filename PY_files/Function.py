

def fun1():
    return fun4()

def fun2(a: int,b:int):
    return a+b


def fun3(a: int,b:int):
    c=a*b
    return c

def fun4():
    return 'running'

print(fun2(7,6))
print(fun3('a',3))
print(fun3([1,2],3))
print(fun1())

print(type(fun1))

my_fun=fun1()

print(my_fun)

fn1= lambda x,y : x+y

print(fn1(2,3))



