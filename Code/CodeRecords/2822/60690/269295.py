num=int(input())
no1=input().split(" ")
no2=input().split(" ")
no1.pop(0)
no2.pop(0)
for i in range(len(no1)): no1[i]=int(no1[i])
for i in range(len(no2)): no2[i]=int(no2[i])
time=0
winner=0
no1_=no1[:]
no2_=no2[:]
while len(no1)!=0 and len(no2)!=0:
    time+=1
    a=no1[0]
    b=no2[0]
    no1.pop(0)
    no2.pop(0)
    if a>b:
        no1.append(b)
        no1.append(a)
    else:
        no2.append(a)
        no2.append(b)
    if no1==no1_ and no2==no2_:
        time=-1
        break
if time>0:
    if len(no1)==0: winner=2
    else: winner=1
    print(str(time)+" "+str(winner))
else:
    print(-1)