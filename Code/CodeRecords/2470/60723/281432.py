T=int(input())
for i in range(T):
    n=int(input())
    temp=input().split()
    array=[[0 for _ in range(n)] for _ in range(n)]
    for j in range(len(temp)):
        array[int(j/n)][j%n]=int(temp[j])
    for j in range(n):
        for k in range(n-1,-1,-1):
            print(array[k][j],end=' ')
    print()