n=(int)(input())
for i in range(n):
    k=(int)(input())
    total=0
    yi=0
    er=0
    num=[int(n) for n in input().split()]
    for index in range(k):
        if num[index]%3==1:
            yi+=1
        elif num[index]%3==2:
            er+=1
        else:
            total+=1
    total+=min(yi,er)
    if yi>er:
        yi=yi-er
        total+=(int)(yi/3)
    elif er>yi:
        er=er-yi
        total+=(int)(er/3)
    print(total)