nums=list(map(int,input().split(",")))
if len(nums)<3:
    print(0)
else:
    sum=0
    for length in range(3,len(nums)+1):
        for start in range(0,len(nums)-length+1):
            jud=True
            gap=nums[start+1]-nums[start]
            for i in range(start,start+length-1):
                if nums[i+1]-nums[i]!=gap:
                    jud=False
                    break
            if jud:
                sum+=1
    print(sum)