import math
list=eval(input())
requestedDay=int(input())

sum=0
biggest=list[0]
for item in list:
    sum+=item
    if item>biggest:
        biggest=item
basic=max(biggest, math.ceil(sum / requestedDay))
result=basic

for i in range(0,biggest):
    temp=0
    day=0
    for item in list:
        temp+=item
        if temp>(basic+i):
            temp=item
            day+=1
            newDay=True
        if list.index(item)==len(list)-1:
            day+=1     # 然后就直接结束了
    if day==requestedDay:
        result=basic+i
        break
print(result)