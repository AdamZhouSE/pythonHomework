def arr14():
    n=int(input())
    riddles=[int(x) for x in input().split(" ")]
    res=0
    unsolved=[]
    for i in range(n):
        unsolved.append(riddles[i])
        if(i==max(unsolved)-1):
            res+=1
    print(res)
    return

arr14()