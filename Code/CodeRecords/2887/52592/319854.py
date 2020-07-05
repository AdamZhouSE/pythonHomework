a=int(input())
l1=[0,0]
l2=[0,0]
count1=0
count2=0
for i in range(a):
    l=[]
    b=[]
    b=input().split()
    for j in range(len(b)):
        l.append(int(b[j]))
    if l[0]==1:
        l1[0]=l1[0]+l[1]
        l1[1]=l1[1]+l[2]
        count1=count1+1
    if l[0]==2:
        l2[0]=l2[0]+l[1]
        l2[1]=l2[1]+l[2]
        count2=count2+1
if l1[0]>=count1*5:
    print("LIVE")
else:
    print("DEAD")
if l2[0]<count2*5:
    print("DEAD")
else:
    print("LIVE")