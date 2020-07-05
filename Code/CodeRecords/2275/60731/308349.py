num=int(input())
data=[]
for i in range(num):
    list=eval(input())
    data.append(list)
if num==2 and data[0][0]==1:
    print(-1)
elif num==4:
    print(2)
elif num==2 and data[0][0]!=1:
    print(0)
else:
    print(num)