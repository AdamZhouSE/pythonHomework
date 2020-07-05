t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    ss=[]
    for i in s:
        ss.append(int(i))
    for j in range(1,n):
        if j not in ss:
            print(j)