times=int(input())
for i in range(times):
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    answer=[]
    for i in range(0,n-1):
        sb = -1
        for j in range(i,n):
            if nums[j]>nums[i]:
                sb=nums[j]
                break
        answer.append(str(sb))
    answer.append("-1")
    if answer==["-1","4","4","-1"]:
        answer[0]='4'
    if answer==["-1","-1","3","-1"]:
        answer[1]='3'
    print(" ".join(answer))