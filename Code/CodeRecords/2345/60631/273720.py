t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    li =[]
    for i in s:
        li.append(int(i))
    s=sorted(li)
    a=0
    b=0
    for j in range(1,n):
        if j not in s:
            a=j
    for j in range(n):
        if s[j]==s[j-1]:
            b=s[j]
    print(b,a)