t=int(input())
m=[]
for i in range(0,t):
    m.append(list(map(int,input().split())))
for i in range(0,len(m)):
    print(m[i][1]**(m[i][0]-1))
  