input()
nums=list(map(int,input().split(' ')))
cnt=int(input())
operations=[]
for i in range(0,cnt):
    operations.append(input())
for str in operations:
    if len(str)==3:
        print(nums[(len(nums)-1)//2])
    else:
        k=int(str[4:])
        nums.append(k)
        nums.sort()