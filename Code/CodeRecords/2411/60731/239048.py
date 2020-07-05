n=int(input())
list=[]
for i in range(n):
    a,b=map(int,input().split(','))
    l=[a,b]
    list.append(l)
p=(list[0][1]-list[1][1])/(list[0][0]-list[1][0])
q=list[0][1]-p*list[0][0]
flag=True
for i in range(n):
    if list[i][0]*p+q!=list[i][1]:
        flag=False
        break
print(flag)