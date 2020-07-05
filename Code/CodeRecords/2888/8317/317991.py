def dealRes():
    nm=input()
    n=int(nm.split(" ")[0])
    m=int(nm.split(" ")[1])
    nums=list(map(int, input().split(" ")))
    #print(nums)
    countp=nums.count(1)
    countm=nums.count(-1)
    index=0
    while index<m:
        lr=input()
        l=int(lr.split(" ")[0])
        r=int(lr.split(" ")[1])
        val=r-l+1
        if val%2==1:
            print(0)
        elif val<=countp and val<=countm:
            print(1)
        else:
            print(0)
        index+=1
        
dealRes()