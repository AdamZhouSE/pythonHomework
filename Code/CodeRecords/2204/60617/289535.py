def recur(x):
    if x==0:
        return
    recur(x-1)
    print(x,end=" ")

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        recur(int(input()))
        print()