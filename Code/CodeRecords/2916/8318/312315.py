def dealRes():
    n=int(input())
    nums=list(map(int, input().split(" ")))
    counts=[]
    arr=[4,8,15,16,32,42]
    for v in arr:
        counts.append(nums.count(v))
    minC=min(counts)
    print(n-minC*6)

dealRes()