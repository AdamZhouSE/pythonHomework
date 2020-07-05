import collections
size=int(input())
nums=list(map(int,input().split(' ')))
nums.insert(0,0)
tmp1=collections.defaultdict(list)
tmp2=collections.defaultdict(list)
for i in range(1,size+1):
    tmp1[nums[i]].append(i)
    tmp2[nums[i]].append(i)
ans=1
flag=False
while True:
    for i in range(1,size+1):
        if(i in tmp1[i]):
            flag=True
            break
    if(flag):
        print(ans)
        break
    for i in range(1,size+1):
        tmp2[nums[i]]+=tmp1[i]
    tmp1=tmp2
    ans+=1



