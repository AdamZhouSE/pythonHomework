N,P = [int(x) for x in input().split()]
A  = [int(x) for x in input().split()]
M= int(input())
for i in range(M):
    this = [int(x) for x in input().split(" ")]
    if(this[0]==1):
        t,g,c = [x-1 for x in this[1:]]
        c+=1
        for j in range(t,g+1):
            A[j] = c*A[j]
    if(this[0]==2):
        t, g, c = [x-1 for x in this[1:]]
        c+=1
        for j in range(t,g+1):
            A[j] = c+A[j]
    if(this[0]==3):
        t,g = [x-1 for x in this[1:]]
        print(sum(A[t:g+1])%P)