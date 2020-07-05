def replace69(N):
    trans=str.maketrans('6','9')
    return N.translate(trans)    




T=int(input())
for i in range(T):
    N=input()
    print(replace69(N))