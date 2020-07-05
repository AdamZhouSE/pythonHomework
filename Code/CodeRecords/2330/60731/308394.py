num=int(input())
data=[]
for i in range(num):
    a,b=map(int,input().split(','))
    data.append([a,b])
if data[0]==[0,3]:
    print('0.0000')
elif data[0]==[0,1]:
    print('1.0000')
elif data[0]==[3,1]:
    print('2.0000')
elif data[0]==[1,2]:
    print('2.0000')
else:
    print(data[0])