import random
r = random.randint(1,20)

while(True):
    a = int(input())
    if(a<r):
        print("write it more than")
    elif(a>r):
        print("write small")
    else:
        print("you guessed it right")
        break;