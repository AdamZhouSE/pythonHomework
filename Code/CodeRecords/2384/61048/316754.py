def arr42():
    n=int(input())
    for i in range(n):
        k=int(input())
        arr=[int(x) for x in input().split(' ')]
        high=max(arr)+2
        if(high<1):
            hish=2
        for j in range(1,max(arr)+2):
            if j not in arr:
                print(j)
                break
    return 

arr42()