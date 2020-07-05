hous=list(map(int,input().split(',')))
warms=list(map(int,input().split(',')))
res=set()
res.add(i for i in warms)
maxsize=0
for house in hous:
    minwarm=abs(house-warms[0])
    for warm in warms:
        minwarm=min(minwarm,abs(house-warm))
    maxsize=max(maxsize,minwarm)

print(maxsize)