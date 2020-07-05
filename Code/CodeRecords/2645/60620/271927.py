import math
piles=eval(input())
h=int(input())
x=sum(piles)//h
def f(k):
    return sum(math.ceil(i/k) for i in piles)<=h
while True:
    if(f(x)):
        print(x)
        break
    else:
        x+=1