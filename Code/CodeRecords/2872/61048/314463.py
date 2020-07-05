def arr9():
    n=int(input())
    stones=[x for x in input()]
    res=0
    for i in range(1,n):
        if(stones[i]==stones[i-1]):
            res+=1
    print(res)
    return

arr9()