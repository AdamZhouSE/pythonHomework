def solve():
    n=int(input())
    getin=list(map(int,input().split()))
    getout=list(map(int,input().split()))
    res=0
    for i in range(n):
        for j in range(i+1,n):
            index1=getin.index(getout[i])
            index2=getin.index(getout[j])
            if index1>index2:
                res+=1
                break
    print(res)

if  __name__ == '__main__' :
    solve()