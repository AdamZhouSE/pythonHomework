def solve():
    arr1=list(map(int,input().split(',')))
    arr2=list(map(int,input().split(',')))
    n=len(arr1)

    def getV(i,j):
        return abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)

    res=0
    for i in range(n):
        for j in range(i+1,n):
            res=max(getV(i,j),res)
    print(res)

if  __name__ == '__main__' :
    solve()