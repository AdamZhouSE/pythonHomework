weights=eval(input())
d=int(input())
re=max(weights)
while True:
    temp=0
    day=0
    for i in range(0,len(weights)):
        if temp+weights[i]<=re:
            temp+=weights[i]
        else:
            day+=1
            temp=weights[i]
        if day>d:
            break
    else:
        if temp==0:
            break
        else:
            day+=1
            if day<=d:
                break
            else:
                re+=1
                continue
    re+=1
print(re)