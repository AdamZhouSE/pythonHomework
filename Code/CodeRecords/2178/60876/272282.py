n=int(input())
num=list(map(int,input().split(" ")))
nums=[]
def ari():
    temp=[]
    length=len(nums)
    for start in range(0,length):
        for end in range(start,length):
            if nums[start:end+1] not in temp:
                temp.append(nums[start:end+1])
    return len(temp)
for i in range(0,n):
    nums.append(num[i])
    print(ari())