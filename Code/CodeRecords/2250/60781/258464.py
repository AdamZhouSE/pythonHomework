n=int(input())
x=0
po=[]
while x<n:
    po.append(input())
    x+=1
t=0
tnew=1
temp=0
count=1
count1=0
while t<n:
    pox=po[t].split(",")
    pox=list(map(int,pox))
    res=pox[1]-pox[0]
    temp=res
    while tnew<n:
        poy = po[tnew].split(",")
        poy = list(map(int, poy))
        res1 = poy[1] - poy[0]
        if(res1==temp):
            count+=1
        tnew+=1

    t+=1
    tnew = t + 1
    if count>count1:
        count1=count
    count=1
print(count1)