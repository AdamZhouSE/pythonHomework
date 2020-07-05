T=int(input())
for i in range(T):
    A1,B1=input().split(' ')
    A=int(A1)
    B=int(B1)
    N=int(input())    
    count=A+(N-1)*(B-A)
    print("{0} {1} {2}".format(A,B,N))
    print(count)