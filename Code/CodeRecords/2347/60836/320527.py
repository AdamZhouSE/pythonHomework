"""
飞行大队有若干个来自各地的驾驶员，专门驾驶一种型号的飞机
这种飞机每架有两个驾驶员，需一个正驾驶员和一个副驾驶员
由于种种原因，例如相互配合的问题，有些驾驶员不能在同一架飞机上飞行，问如何搭配驾驶员才能使出航的飞机最多
因为驾驶工作分工严格，两个正驾驶员或两个副驾驶员都不能同机飞行
"""

NM=[int(m) for m in (str(input()).strip()).split(" ")]
N=NM[0]
M=NM[1]

arr=[]
while True:
    line = input()
    if line:
        arr.append([int(m) for m in (str(line).strip()).split(" ")])
    else:
        break

busy=[False for i in range(N)]

i=0
num=0
while(i<len(arr)):
    a=arr[i][0]-1
    b=arr[i][1]-1
    if(not busy[a] and not busy[b]):
        busy[a]=True
        busy[b]=True
        num+=1
    i+=1
print(num)