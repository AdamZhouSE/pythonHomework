def continous1():
    N=int(input())
    res=0
    # if N==1:
    #     print(0)
    #     return
    # DP=[0]*(N+1)
    # DP[2]=N-2+1
    # for i in range(3,N):
    #     DP[i]=DP[i-1]*(N-(i-1))-(N-i+1)
    # DP[N]=1
    # res=0
    # for i in range(2,N+1):
    #     res+=DP[i]
    # print(res)
    for i in range(0,2**N+1):
        temp=bin(i)[2:]
        for i in range(0,len(temp)-1):
            if temp[i]=='1' and temp[i+1]=='1':
                res+=1
                break
    print(res)
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        continous1()