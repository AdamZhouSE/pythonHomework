n=int(input())
for i in range(n):
    line=input().split()
    N=int(line[0])
    M=int(line[1])
    K=int(line[2])
    line=input().split()
    a=list(map(int, line))
    line=input().split()
    b=list(map(int, line))
    c=a+b
    c=sorted(c)
    print(c[K-1])