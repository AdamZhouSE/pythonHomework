def replace69(N):
    trans=str.maketrans('6','9')
    a=N.translate(trans)
    return int(a)-int(N)




T=int(input())
for i in range(T):
    N=input()
    print(replace69(N))