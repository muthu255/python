def fun(a,b,*c):
    return a,b,c

def avg(*args):
    count=len(args)
    total=sum(args)
    return total/count
    

print(fun(1,2,3,4))


print(avg(1,2,3,4))

