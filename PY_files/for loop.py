s='Muthu'
k=(1,2,3,4,5,6)
a=0

print('========Excercise1==========')
for i in s:
    print(a,i)
    a+=1
print('========Excercise2==========')
for i in range(len(s)):
    print(i,s[i])

print('========Excercise3==========')

for i in range (1,5):
    print(i)

print('========Excercise4==========')
for i,j in [(1,2),(2,3),(4,5)]:
    print(i,'->',j)
print('========Excercise5==========')

for i in k:
    if i%2==0:
        print(i,'-> divisible by 2')
    else:
        print(i,'-> Not divisible by 2')
print('======END======')
    

    
