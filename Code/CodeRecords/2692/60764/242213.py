goods=eval(input())
day=int(input())
res=max(goods)
while True:
    sums=0
    i=0
    j=1
    while j<=len(goods):
        if sum(goods[i:j])<=res:
            j+=1
        else:
            sums+=1
            i=j-1
    sums+=1
    if sums>day:
        res+=1
    else:
        break
print(res)