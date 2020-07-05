import math
def stTable():
    row=input().split(" ")
    N=int(row[0])
    M=int(row[1])
    wordList=[]
    queryLi=[]
    bi=[0 for i in range(0,12)]
    for i in range(0,12):
        bi[i]=2**i
    for i in range(0,N):
        wordList.append(input())
    for i in range(0,M):
        queryLi.append(list(map(int,input().split(" "))))
    st=[["null" for i in range(0,12)] for i in range(0,1000)]
    for i in range(1,N+1):
        st[i][0]=wordList[i-1]
    j=1
    while 2**j<=N:
        i=1
        while i+2**(j-1)<=N:
            st[i][j]=max(st[i][j-1],st[i+2**(j-1)][j-1])
            i+=1
        j+=1
    for query in queryLi:
        l=query[0]
        r=query[1]
        lg=int(math.log2(r-l+1))
        print(max(st[l][lg],st[r-2**lg+1][lg]))

if __name__=='__main__':
    stTable()