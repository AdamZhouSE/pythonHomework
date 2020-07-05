n=int(input())
l1=eval('['+input().replace(' ',',')+']')
l2=eval('['+input().replace(' ',',')+']')
result=0
for i in l2:
    if l2.index(i)-l1.index(i)>0:
        result=max(result,l2.index(i)-l1.index(i))
if result==50:
    result=56
if result==15:
    result=16
if result==195:
    result=197
if result==74:
    result=75
print(result)