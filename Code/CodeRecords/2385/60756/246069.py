T=int(input())
for i in range(T):
    N=int(input())
    zero=1
    one=1
    for j in range(1,N):
        zero=zero+one
        one=zero-one
    print(zero+one)