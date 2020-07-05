def dealRes():
    n=int(input())
    numStr=input().split(" ")
    nums=list(map(int, numStr))
    res=sum(nums)%2
    if res==0:
        print("YES")
    else:
        print("NO")
        
dealRes()