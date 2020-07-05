n=int(input())
list=[]
for i in range(n):
    a,b=map(int,input().split(','))
    l=[a,b]
    list.append(l)
flag=True
if list[0]==list[1] or list[1]==list[2] or list[0]==list[2]:
    flag=False
if (list[0][0]==list[1][0] and list[1][0]==list[2][0]) or(list[0][1]==list[1][1] and list[1][1]==list[2][1]):
    flag=False
if (list[0][1]-list[1][1])/(list[0][0]-list[1][0])==(list[2][1]-list[1][1])/(list[2][0]-list[1][0]):
    flag=False
print(flag)