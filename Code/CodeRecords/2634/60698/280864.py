def test():
    nums=list(eval(input()))
    k=int(input())
    res=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                res.append([nums[i],nums[j],nums[i]/nums[j]])
    res.sort(key=lambda x:x[2])
    answer=res[k-1]
    print(answer[0:2])


test()
