def tb18():
    n=int(input())
    for j in range(n):
        k=int(input())
        mice=[int(x) for x in input().split(' ')]
        holes=[int(x) for x in input().split(' ')]
        mice.sort()
        holes.sort()
        res=0
        for i in range(k):
            res=max(res,holes[i]-mice[i])
        print(res)

    return

tb18()