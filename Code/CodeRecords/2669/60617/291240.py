def digitAnd():
    N=int(input())
    for i in range(N,-1,-1):
        if N&i==i:
            print(i,end=" ")
    print()
    
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        digitAnd()