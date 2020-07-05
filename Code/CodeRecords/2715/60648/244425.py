def removeStones(stones):

    UF = {}

    def find(x):

        if x != UF[x]:

            UF[x] = find(UF[x])

        return UF[x]

        

    def union(x, y):

        UF.setdefault(x, x)

        UF.setdefault(y, y)

        UF[find(x)] = find(y)



    for i,j in stones:

        union(i, ~j)

    return len(stones) - len({find(x) for x in UF})



if __name__ == "__main__":    
    stones=input().strip('[]').split("], [")
    stones=[i.split(",") for i in stones]
    l=len(stones) 
    for i in range(l):
        for j in range(l):
            stones[i][j]=int(stones[i][j])            
    x=removeStones(stones)
    
    print(x)