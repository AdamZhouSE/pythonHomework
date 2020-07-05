n=int(input())
coins=list(map(int,input().split(" ")))

count={}

maxNum=1
for i in coins:
    if i in count:
        count[i]+=1
        maxNum=max(maxNum,count[i])
    else:
        count[i]=1
print(maxNum)