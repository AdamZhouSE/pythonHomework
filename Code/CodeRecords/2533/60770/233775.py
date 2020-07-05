def solve():
    A = list(map(int, input()[1:-1].split(',')))
    front=0
    behind=len(A)-1
    while True:
        while A[front]%2==0:
            front+=1
        while A[behind]%2==1:
            behind-=1
        if front<behind:
            temp=A[front]
            A[front]=A[behind]
            A[behind]=temp
        else: break
    print(A)

if  __name__ == '__main__' :
    solve()