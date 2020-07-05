a=int(input())
for i in range(0,a):
    c=int(input())
    d=[int(i) for i in input().split()]
    d.sort()
    if c%2==1:
        print(d[c//2])
    else:
        nums=(d[c//2-1]+d[c//2])//2
        print(nums)
