a=list(map(int,input().replace('[','').replace(']','').split(',')))
n=int(input())
if n not in a:
    print(-1)
else:
    print(a.index(n))