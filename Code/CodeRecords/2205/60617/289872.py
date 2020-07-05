def shakeHands():
    N=int(input())
    if N==2:
        print(1)
        return 
    else:
        ways=[0]*(N+1)
        ways[0]=1
        ways[2]=1
        for i in range(4,N+1,2):
            for j in range(2,i+1,2):
                ways[i]+=ways[j-2]*ways[i-j]
    print(ways[N])

if __name__=='__main__':
    T=int(input())
    for i in range(0, T):
        shakeHands()