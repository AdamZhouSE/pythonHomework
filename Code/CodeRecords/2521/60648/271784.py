import random
l=eval(input())
a=0
while a==0:
    random.shuffle(l)
    count=0
    for i in range(len(l)-1):
        if l[i]!=l[i+1]:
            count+=1
    if count==len(l)-1:
        print(l)
        break