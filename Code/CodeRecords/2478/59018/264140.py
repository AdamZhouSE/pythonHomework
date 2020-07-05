T=int(input())                        #给出的是等差数列第一项和第二项 即a1 a2
for i in range(T):
    A1,B1=input().split(' ')
    A=int(A1)
    B=int(B1)
    N=int(input())    
    count=A+(N-1)*(B-A)
    print(count)