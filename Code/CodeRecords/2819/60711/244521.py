import re


num=input()
All=input()
result=0
one=0
two=0
three=0
group=re.compile('\d+').findall(All)
for x in range(int(num)):
    if group[x]=='4':result+=1
    if group[x]=='3':three+=1
    if group[x]=='2':two+=1
    if group[x]=='1':one+=1

if three>=one:
    result=result+three+ two//2+ two%2
else:
    if two%2+(one-three)%4==0:
        result=result+three+two//2+(one-three)//4
    else:
        if two%2+(one-three)%4==5:
            result = result + three + two // 2 + (one - three) // 4+2
        else:
            result = result + three + two // 2 + (one - three) // 4+1

print(result)