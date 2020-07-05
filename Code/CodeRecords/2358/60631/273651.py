t=int(input())
for ti in range(t):
    si=input().split(' ')
    n=int(si[0])
    k=int(si[1])
    s=input().split(' ')
    li=[]
    for i in s:
        li.append(int(i))
    li=sorted(li,reverse=True)
    for j in range(k):
        print(li[j],end=' ')
    print()