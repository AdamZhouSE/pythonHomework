def dealRes():
    n=int(input())
    nums=list(map(int, input().split(" ")))
    count1=nums.count(1)
    count2=nums.count(2)
    res=0
    if count1>=count2:
        res = res+count2+int((count1-count2)/3)
    else:
        res+=count1
    print(res)
    
dealRes()