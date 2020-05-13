import random

mk=['muthu','krish']
def sample():
    #print('I love you')
    #print('I @E')
    return random.choices(mk)

def sample1():
    for i in range(5):
        print(sample(), end='\r')
print()
     
    
def iadd(*args):
    t=0
    for i in args:
        t+=i
    return t
#print()




def keywds(**ilist):
    for i in ilist:
        print(i,'->',ilist[i])
    return tuple(ilist.values())


ilist={'mk':'muhtu','jn':'john','ms':'surya'}
print(keywds(**ilist))



def myFun(**kwargs):  
    for key,value in kwargs.items(): 
        print ('%s%s'%(key,value))
    return 0
  
# Driver code 
print(myFun(first ='Geeks', mid ='for', last='Geeks'))

#sample()
#sample1()  
#m=(1,2,3,4,5,6)
#print('iadd(args)->',iadd(*m))







