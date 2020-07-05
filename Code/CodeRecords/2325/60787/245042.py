def hcf(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            re=i
    return re

card=sorted(input().split(","))
card=[int(i) for i in card]
num=[]
temp=1
for i in range(0,len(card)-1):
    if card[i]==card[i+1]:
        temp+=1
    else:
        num.append(temp)
        temp=1
    if i==len(card)-1:
        num.append(temp)
num=sorted(num)
if len(num)==0:
    print(False)
elif max(num)<2:
    print(False)
elif len(num)==1:
    print(True)
else:
    temp=hcf(num[0],num[1])
    for i in range(2,len(num)):
        temp=hcf(temp,num[i])
    if temp<2:
        print(False)
    else:
        print(True)