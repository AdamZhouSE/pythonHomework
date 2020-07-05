def dealRes():
    n=int(input())
    nums=list(map(int, input().split(" ")))
    maxN=0
    ontable=[]
    for val in nums:
        if val in ontable:
            ontable.pop(ontable.index(val))
        else:
            ontable.append(val)
        maxN=len(ontable) if len(ontable)>maxN else maxN
    print(maxN)
    
    
dealRes()