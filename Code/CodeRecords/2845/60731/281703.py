n=int(input())
qualitySet=[0]*(n+3)
flag=False
for i in range(n):
    price,quality=map(int,input().split())
    qualitySet[price-1]=quality
for i in range(n-1):
    if qualitySet[i+1]<qualitySet[i]:
        flag=True
        print('Happy Alex')
        break
if not flag:
    print('Poor Alex')