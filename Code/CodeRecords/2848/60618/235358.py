nA,nB = map(int,input().split())
k,m=map(int,input().split())
A=[int(n) for n in input().split()]
B=[int(n) for n in input().split()]
    
min = B[len(B)-k]
max=A[m-1]

if nA>=k and nB>=m:
    if min >max:
        print("YES")
    else:
        print("NO")
else:
    print("NO")