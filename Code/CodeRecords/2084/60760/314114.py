def func(n:int,maps:list,start:int,end:int):
    res=[99999]*n
    res[start-1]=0
    ishave=[start]
    begins=[start]
    temp=[]
    while len(ishave)<n:
        for i in maps:
            for j in begins:
                if i[0]==j and res[j-1]+i[2]<res[i[1]-1]:

                    res[i[1]-1]=res[j-1]+i[2]
                    if ishave.count(i[1])==0:
                        ishave.append(i[1])
                    if temp.count(i[1])==0:
                        temp.append(i[1])
                    
        begins=(list(temp))
        temp.clear()
    return res[end-1]
first=list(map(int,input().split(' ')))
n=first[0]   #顶点数
m=first[1]   #边数
s=first[2]   #目标路径开始顶点
t=first[3]   #目标路径结束顶点
maps=[]
for i in range(m):  #第一个数是开始顶点，第二个数是结束顶点，第三位是路长
    maps.append(list(map(int,input().split(' '))))
print(func(n,maps,s,t))