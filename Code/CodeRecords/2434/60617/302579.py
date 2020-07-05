import math
def silenceProblem():
    row=input().split(" ")
    n=int(row[0])
    m=int(row[1])
    c=int(row[2])
    bi=[0]*12
    flag=False
    for i in range(0,11):
        bi[i]=2**i
    sequence=list(map(int,input().split(" ")))
    lg=int(math.log2(m))
    st1=[[0 for i in range(0,10)] for i in range(0,10000)]
    st2=[[2**16 for i in range(0,10)] for i in range(0,10000)]
    for i in range(1,n+1):
        st1[i][0]=sequence[i-1]
        st2[i][0]=sequence[i-1]

    for i in range(1,int(lg)+1):
        j=1
        while j+bi[i]-1<=n:
            st1[j][i]=max(st1[j][i-1],st1[j+bi[i-1]][i-1])
            j+=1
    for i in range(1,int(lg)+1):
        j=1
        while j+bi[i]-1<=n:
            st2[j][i]=min(st2[j][i-1],st2[j+bi[i-1]][i-1])
            j+=1
    for i in range(1,n-m+2):
        if max(st1[i][lg],st1[i+m-bi[lg]][lg])-min(st2[i][lg],st2[i+m-bi[lg]][lg])<=c:
            flag=True
            print(i)
    if not flag:
        print(-1)

if __name__=='__main__':
    silenceProblem()