n=int(input())
nums=list(map(int,input().split(" ")))

minNum=min(nums)
tmp=n//minNum
if minNum>n:
    print(-1)
else:
    res=0
    i=0
    while i<tmp:
        res=10*res+nums.index(minNum)+1
        n-=nums[nums.index(minNum)]
        i+=1
    init_index=res%10-1
    if init_index<9:
        times=0
        while times<len(str(res)) and minNum+n>=min(nums[init_index+1:]):
            i=8
            while i>init_index:
                if nums[i]<=minNum+n:
                    temp=str(res)
                    res=int(temp[0:times]+str(i+1)+temp[times+1:])
                    n-=nums[i]-nums[init_index]
                    times+=1
                    break
                i-=1

    print(res)