t=int(input())
m=[]
for i in range(0,t):
    m.append(list(map(int,input().split())))
for i in range(0,len(m)):
    x=0
    for j in range(1,m[i][0]+1):
        x+=j**5
    print(x)