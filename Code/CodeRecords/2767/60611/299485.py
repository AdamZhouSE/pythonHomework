from collections import Counter
num=int(input())
for i in range(num):
    target=int(input())
    number=0
    count=[]
    for j in range(target//3):
        c=[j]
        if (target-3*j)%5==0:
            c.append((target-3*j)//5)
            count.append(c)
    number+=len(count)
    for j in count:
        if j[1]>1:
            number+=j[1]//2
    print(number)