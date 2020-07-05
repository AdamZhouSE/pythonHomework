weight=eval(input())
day=int(input())
upper=sum(weight)
lower=max(upper//day,max(weight))

while lower<=upper:
    m,need,now=(lower+upper)//2,1,0
    for i in weight:
        if now+i>m:
            need=need+1
            now=0
        now=now+i
    if need>day:
        lower=m+1
    else:
        upper=m-1
print(lower)