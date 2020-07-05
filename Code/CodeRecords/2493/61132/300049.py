t = int(input())
l=list(map(int,input().split()))
t = int(input())
for j in range(t):
    n1,n2=map(int,input().split())
    print(len(set(l[n1-1:n2])))