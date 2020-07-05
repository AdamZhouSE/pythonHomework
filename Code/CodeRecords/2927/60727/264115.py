def jug(n,d,p):
    x=p[0]
    y=p[1]
    if y>=d-x and y<=2*n-d-x and y>=x-d and y<=x+d:
        return 'YES'
    else:
        return 'NO'
    
x=input().split(' ')
n=int(x[0])
d=int(x[1])
num = int(input())
for i in range(0,num):
    data=input()
    data=data.split(' ')
    data=list(map(int,data))
    print(jug(n,d,data))
