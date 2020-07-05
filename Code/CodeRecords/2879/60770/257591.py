def solve():
    n=int(input())
    n2=int(pow(n,2))
    cross=[]
    for i in range(n2):
        cross.append(list(map(int,input().split())))
    row,col=set(),set()
    days=[]
    for i in range(n2):
        if not(cross[i][0] in row) and not(cross[i][1] in col):
            days.append(i+1)
            row.add(cross[i][0])
            col.add(cross[i][1])
    res=list(map(str,days))
    print(" ".join(res))

if  __name__ == '__main__' :
    solve()