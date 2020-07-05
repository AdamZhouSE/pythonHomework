orderNum=int(input().strip())
data=[]
for i in range(orderNum):
    puts=input().strip().split(' ')
    puts=[int(j) for j in puts]
    data.append(puts)
#服务器数量
count1=0
count2=0
#成功数量
count1Success=0
count2Success=0
for i in data:
    if i[0]==1:
        count1+=1
        count1Success+=i[1]
    if i[0]==2:
        count2+=1
        count2Success+=i[1]

if count1Success>=count1*5:
    print('LIVE')
else:
    print("DEAD")
if count2Success>=count2*5:
    print('LIVE')
else:
    print("DEAD")
