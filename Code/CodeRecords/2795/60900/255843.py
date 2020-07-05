import math
n = input()
str = input().split(" ")
for i in range (0,int(n)):
    str[i] = int(str[i])

str = list(set(str))
cha=[]
for i in range(0,len(str)-1):
    cha1 =1000000000
    for j in range(i+1,len(str)):
        if int(math.fabs(str[i]-str[j]))<cha1:
            cha1 = int(math.fabs(str[i]-str[j]))
    cha.append(cha1)


cha = list(set(cha))
cha2 =[]
for i in range(0,len(cha)):
    if cha[i]!=0:
        cha2.append(cha[i])


if (len(cha2)==1):
    print(cha2[0])
else:
    print("-1")