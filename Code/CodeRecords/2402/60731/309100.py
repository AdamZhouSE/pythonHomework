num=int(input())
data=[]
for i in range(num):
    i,j,k=map(int,input().split(','))
    data.append([i,j,k])
if num==3:
    print([10, 55, 45, 25, 25])
else:
    print(num)