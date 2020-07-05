t=int(input())
ans=[]
for i in range(t):
    nm=input().split(' ')
    n=int(nm[0])
    m=int(nm[1])
    a=input().split(' ')
    a=list(map(int,a))
    a=set(a)
    b=input().split(' ')
    b=list(map(int,b))
    b=set(b)
    ans.append(len(a&b))
for k in ans:
    print(k)