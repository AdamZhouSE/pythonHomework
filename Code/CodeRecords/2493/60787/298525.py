n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
for q in range(0,m):
    temp=[]
    l,r=map(int,input().split())
    for i in range(l-1,r):
        if not a[i] in temp:
            temp.append(a[i])
    print(len(temp))