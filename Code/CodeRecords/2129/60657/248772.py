import math
n=int(input())
cons=0
def Judge(a):
    while a > 1:
        a = a / 2
    if a == 1:
        return True
    else:
        return False
while(n>1):

    if(n%2==0):
        n=n//2
        cons+=1
        if(Judge(n)):
            cons+=math.log(n,2)
            break
    elif(n==3):
        cons+=2
        break
    else:
        if(Judge(n+1)):
            n=n+1
            cons+=1
        elif(Judge(n-1)):
            n=n-1
            cons += 1
        elif(((n-1)/2)%2==0):
            n=n-1
            cons += 1
        elif(((n+1)/2)%2==0):
            n = n + 1
            cons += 1
print(int(cons))
