length=int(input())
nums=list(map(int,input().split(" ")))
nums.sort()
minus=[]
zero=[]
plus=[]
for item in nums:
    if item<0:
        minus.append(item)
    elif item==0:
        zero.append(item)
    else:
        plus.append(item)
if len(minus)%2==0:
    sum=0
    for item in nums:
        if item<0:
            sum+=(-1-item)
        elif item==0:
            sum+=1
        else:
            sum+=(item-1)
    print(sum)
elif len(zero)!=0:
    sum=len(zero)
    for item in minus:
        sum+=(-1-item)
    for item in plus:
        sum+=(item-1)
    print(sum)
else:
    minus.sort()
    plus.sort()
    lenm=len(minus)
    lenp=len(plus)
    min=plus[0]+1
    if (1-minus[lenm-1])<min:
        min=1-minus[lenm-1]
        del minus[lenm-1]
        for item in minus:
            min+=(-1-item)
        for item in plus:
            min+=(item-1)
        print(min)
    else:
        del plus[0]
        for item in minus:
            min+=(-1-item)
        for item in plus:
            min+=(item-1)
        print(min)