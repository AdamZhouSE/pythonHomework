t=int(input())
a=[]
for i in range(t):
    a.append(input().split(' '))
for i in range(t):
    b=int(a[i][0],2)
    c=int(a[i][1],2)
    print(b*c)
    
    