t=int(input())
while t:
    line=[int(x) for x in input().split()]
    x=line[1]
    nums=[int(x) for x in input().split()]
    ret=0
    for num in nums:
        if num%x==0:
            ret=ret|num
    print(ret)
    t-=1