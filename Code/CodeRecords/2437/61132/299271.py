n,k=map(int,input().split())
yl=[0]
indexy=0
for j in range(n):
    num,dire=input().split()
    num=int(num)
    if dire=='R':
        for i in range(num):
            if indexy<len(yl):
                yl[indexy]+=1
            else:
                yl.append(1)
            indexy += 1
    else:
        for i in range(num):
            if indexy>=0:
                indexy-=1
                yl[indexy]+=1
            else:
                yl.insert(0,1)
yl=[1 if i>=k else 0 for i in yl]
print(sum(yl))