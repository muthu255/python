i=0

while i<10:
    print(i)
    i+=1

while True:
    print(i)
    if i <=10:
        break

min_length=2
name=input('please enter the name :')
while not(len(name)>min_length and name.isprintable() and name.isalpha()):
    name=input('please enter the name :')
        
print("hello,{0}".format(name))


min_length=2
while True:
    name=input('please enter the name :')
    if len(name)>min_length and name.isprintable() and name.isalpha():
        break
print("hello,{0}".format(name))


b=0
while b<=10:
    b+=1
    if b%2==0:
        continue
    print(b)


    
