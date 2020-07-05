danci=input()
danci=danci.replace("[\"","")
danci=danci.replace("\"]","")
shijian=danci.split("\",\"")
for i in range(0,len(shijian)):
    temp=shijian[i].split(':')
    hour=int(temp[0])
    minite=int(temp[1])
    shijian[i]=hour*60+minite
result=[]
for i in range(0,len(shijian)-1):
    for j in range(i+1,len(shijian)):
        result.append(max(shijian[i],shijian[j])-min(shijian[i],shijian[j]))
print(min(min(result),1440-max(result)))