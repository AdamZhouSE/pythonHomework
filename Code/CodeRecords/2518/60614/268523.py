length=len(input().split(','))
heaters=[int(x) for x in input().split(',')]
max=0
for i in range(0,len(heaters)):
    if i==0:
        temp=heaters[0]-1
        if temp>max:
            max=temp
    if i==len(heaters)-1:
        temp=length-heaters[i]
        if temp>max:
            max=temp
    else:
        temp=heaters[i+1]-heaters[i]
        if temp>max:
            max=temp
print(max)