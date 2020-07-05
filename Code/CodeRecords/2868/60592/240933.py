total = int(input())
nums = list(map(int,input().split(' ')))
res = [0,0]
for i in range(0,total):
    if nums[i]%2==0:
        res[0]+=1
    else:
        res[1]+=1
if res[0]>res[1]:
    print(res[1])
else:
    print(res[0])