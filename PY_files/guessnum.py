import random


name=input('Enter the name',)


print('hello '+name.upper()+' please guess the num between 1 to 20')


sceretnum=random.randint(1,20)

for i in range(1,6):
    guess=int(input('take a guess'))

    if guess>sceretnum:
        print('your guess is too high')
    elif guess<sceretnum:
        print('you guess is low')
    else:
        break

if guess==sceretnum:
    print('Good job! '+name+' you guessed my num in '+str(i)+' guesses......')
else:
    print('The num I was thinking was' + str(sceretnum))




