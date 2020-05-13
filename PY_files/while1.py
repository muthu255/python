
l=[1,2,10]
m=88
x=0
while x<len(l):
    if l[x]==m:
        break
    x+=1
else:
    l.append(m)
print(l)

