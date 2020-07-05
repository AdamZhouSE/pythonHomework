def exchange_OddEven():
    N=int(input())
    biN=bin(N)[2:]
    if len(biN)%2!=0:
        biN="0"+biN
    res=["1"]*len(biN)
    for i in range(0,len(biN)):
        if i%2==0:
            res[i]=biN[i+1]
        else:
            res[i]=biN[i-1]
    print(int("".join(res),2))
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        exchange_OddEven()