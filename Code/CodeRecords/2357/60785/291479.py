t=int(input())
for er in range(t):
    n,m,x=[int(i)  for i in input().split()]
    a,b=[int(i)  for i in input().split()],[int(i)  for i in input().split()]
    for i in a:
        for j in b:
            if i+j==x:
                print(i,j)
    