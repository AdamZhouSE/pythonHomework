import math

l=eval(input())
h=int(input())
k=sum(l)//h
while True:
    if sum([math.ceil(i/k) for i in l])<=h:
        print(k)
        break
    k+=1
