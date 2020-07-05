def exchange_digit():
    N=int(input())
    num=bin(N)[2:]
    new="1"*len(num)
    res=0
    for i in range(0,len(new)):
        res+=2**i
    print(res-N,end=" ")
    print(res)
    
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        exchange_digit()