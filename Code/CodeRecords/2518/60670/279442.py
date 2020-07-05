house=list(map(int,input().split(',')))
sun=list(map(int,input().split(',')))
dis=0
for i in house:
    minn=1000000001
    for j in sun:
        if abs(i-j)<minn:
            minn=abs(i-j)
    if minn>dis:
        dis=minn
print(dis)