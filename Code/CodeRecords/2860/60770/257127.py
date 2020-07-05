def solve():
    total=int(input())
    heaps=[]
    rowSet=set()
    colSet=set()
    for i in range(total):
        heaps.append(list(map(int,input().split())))
    res=-1
    for i in range(total):
        if not(heaps[i][0] in rowSet) and not(heaps[i][1] in colSet):
            res+=1
        rowSet.add(heaps[i][0])
        colSet.add(heaps[i][1])
    print(res)

if  __name__ == '__main__' :
    solve()