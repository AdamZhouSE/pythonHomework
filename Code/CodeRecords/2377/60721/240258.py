n=int(input())
list=[None]*n
for i in range(0,n):
    list[i]=input().split(",")
for i in range(0,len(list)):
    for j in range(0,len(list[0])):
        list[i][j]=int(list[i][j])
k=(list[0][1]-list[1][1])/(list[0][0]-list[1][0])
b=list[0][1]-k*list[0][0]
if list[0]==list[1] or list[1]==list[2] or list[0]==list[2]:
    print(False)
elif(list[2][1]==k*list[2][0]+b):
    print(False)
else:
    print(True)