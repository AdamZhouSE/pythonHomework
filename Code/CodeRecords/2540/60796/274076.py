def bubble(ls):
    for i in range(len(ls)):
        j=0
        while j<=len(ls)-2-i:
            if ls[j][1]>ls[j+1][1] or (ls[j][1]==ls[j+1][1] and ls[j][0]>ls[j+1][0]) or( ls[j][0]==ls[j+1][0] and ls[j][1]==ls[j+1][1] and ls[j][2]>ls[j+1][2]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls

nums=input().split(" ")
K=int(nums[0])#奶牛的组数
N=int(nums[1])#地点的个数
C=int(nums[2])#班车的容量
ls=[]
for i in range(K):
    ls.append(input().split(" "))
    ls[i][0]=int(ls[i][0])
    ls[i][1]=int(ls[i][1])
    ls[i][2]=int(ls[i][2])
i=0
while i<len(ls):
    if ls[i][0]>ls[i][1]:
        del ls[i]
        i=i-1
    i=i+1
K=len(ls)
ls=bubble(ls)

InCar=[]#每一组上车的奶牛的数量
for i in range(K):
    InCar.append(0)
cowInCar=0#经过这站后车上的奶牛数
station=1
while station<N+1:
    #print("到了第",station,"站")
    # 此时车上所有可以下车的奶牛下车
    down=0
    i=0
    while i<len(ls):
        if ls[i][1]==station:
            down=down+InCar[i]
        i=i+1
    cowInCar=cowInCar-down
    #print("下车",down,"个",end=' ')
    #所有在此站点上车的奶牛上车
    i=0
    up=0
    while i<len(ls):
        if ls[i][0]==station and ls[i][2]<=C:
            up=up+ls[i][2]
            InCar[i]=ls[i][2]
        i=i+1
    cowInCar=cowInCar+up
    #print("上车",up,"个",end=' ')
    #print("此时车上有", cowInCar,end=' ')
    #如果超过数量，将所有最远目的地且还未下车的奶牛赶下车
    if cowInCar>C:
        i=len(InCar)-1
        while i>=0:
            if InCar[i]>0 and ls[i][1]>station:
                if cowInCar-InCar[i]<=C:
                    InCar[i]=InCar[i]-(cowInCar-C)
                    cowInCar=C
                    break
                else:
                    cowInCar=cowInCar-InCar[i]
                    InCar[i]=0
            if cowInCar==C:
                break
            i=i-1
    #print("此时车上有",cowInCar)
    #print(InCar)
    station=station+1
result=0
for i in range(len(InCar)):
    #print("有",InCar[i],"只奶牛从",ls[i][0],"到",ls[i][1])
    result=result+InCar[i]

print(result)















