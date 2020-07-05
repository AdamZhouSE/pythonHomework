n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
i=0
re=0
count4=0
count3=0
count2=0
count1=0
while i<len(ls):
    if ls[i]==1:
        count1=count1+1
    if ls[i]==2:
        count2=count2+1
    if ls[i]==3:
        count3=count3+1
    if ls[i]==4:
        count4=count4+1
    i=i+1

re=re+count4
count4=0
re=re+int(count2/2)
count2=count2%2#队伍人数为2的要么还有1个要么没有了

if count3==count1:
    re=re+count1
    count1=0
    count3=0
elif count3>count1:
    re=re+count1
    count3=count3-count1
    count1=0
elif count1>count3:
    re=re+count3
    count1=count1-count3
    count3=0

if count3>0:
    re=re+count3
    count3=0
if count2==1:
    count1=count1-2
    re=re+1
if count1>0:
    if count1%4==0:
        re=re+int(count1/4)
    else:
        re=re+int(count1/4)+1
print(re)



