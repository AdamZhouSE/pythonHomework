def rotate(a,n):
    real = []
    after = []
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append(a[x*n+y])
        real.append(temp)
    after = []
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append(real[n-y-1][x])
        after.append(temp)
    pri(after,n)
def pri(after,n):
    for x in range(n):
        for y in range(n):
            print(after[x][y],end=' ')
    print()    
T = int(input())
N,A = [],[]
x = 0
while(x<T):
    x+=1
    N.append(int(input()))
    A.append([int(i) for i in input().split()])
for i in range(T):
    A[i] = rotate(A[i],N[i])
