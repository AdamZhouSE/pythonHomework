case=int(input())
for i in range(case):
    para=[int(x) for x in input().split(' ')]
    a=[int(x) for x in input().split(' ')]
    b=[int(x) for x in input().split(' ')]

    res=a+b
    res.sort()
    print(res[para[2]-1])