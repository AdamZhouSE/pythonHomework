ex=int(input())
while ex>0:
    ex -= 1
    result=0
    len=int(input())
    nums=list(map(int,input().split()))
    for i in range(len):
        for j in range(i,len):
            if nums[i]>nums[j]:
                result += 1
    print(result)