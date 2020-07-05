t=int(input())
a=[]
for i in range(t):
    a.append(list(map(int,input().split(' '))))
for i in range(t):
    size=a[i][0]
    nums=a[i][1]
    res=nums*(int((size+1)/2))
    print(res)