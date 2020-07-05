tests = list(map(int,input().split()))
nums = list(map(int,input().split()))
comd = tests[1]
tem = []
for i in range(0,len(nums)):
    tem.append([nums[i],i])
for i in range(0,comd):
    ls = list(map(int,input().split()))
    tmp = tem[ls[0]-1:ls[1]]
    tmp.sort()
    print(tmp[ls[2]-1][0])