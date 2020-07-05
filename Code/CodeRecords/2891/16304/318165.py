def dealRes():
    n=int(input())
    numStr=input().split(" ")
    nums = list(map(int, numStr))
    maxVal=max(nums)
    count=0
    for val in nums:
        count=count+(maxVal-val)
        
    print(count)
    
    
dealRes()