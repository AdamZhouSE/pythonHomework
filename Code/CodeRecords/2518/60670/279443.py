house=list(map(int,input().split(',')))
sun=list(map(int,input().split(',')))
dis=0
for i in house:
    minn=1000000001
    for j in sun:
        minn=min(minn,abs(i-j))
    dis=max(dis,minn)
print(dis)