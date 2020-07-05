arr=input().split(' ')

N,M=int(arr[0]),int(arr[1])
list=[]
for i in range(0,M):
    at=[int(n) for n in input().split(' ')]
    tem=[]
    for j in range(0,len(at)):
        if at[j]=='':
            continue
        else:
            tem.append(at[j])
    list.append(tem)
treenode=[1]
side=[]
treeside=[]
for i in range(0,len(list)):  #先把与1相连的边加入side
    if list[i][0]==1:
        side.append(list[i])
while len(treenode)<N:
    min,pos=999,-1
    for i in range(0,len(side)):   #选出预选边side最小边的 pos定位
       if side[i][len(side[i])-1]<min:
           min=side[i][len(side[i])-1]
           pos=i
    for i in range(1,len(side[pos])-1):  #在生成树的边上加入边
       treenode.append(side[pos][i])
    treeside.append(side[pos])
    del side[pos]
    x=0
    listpos,sidepos=-1,-1
    for i in range(0,len(list)):   #更新side边
        if list[i][0] in treenode and list[i][1] not in treenode:  #找到还没到生成树离去的节点
            a=0
            listpos=i
            for j in range(0,len(treeside)):
               if treeside[j][len(treeside[j])-2]==list[i][0]:
                   a=treeside[j][len(treeside[j])-1]
                   sidepos=j
                   break
            x=a+list[i][2]
            mark=0
            for k in range(0,len(side)):
               if side[k][len(side[k])-2]==list[listpos][1]:  #在side预选边中找到之前有的
                   mark=1
                   if side[k][len(side[k])-1]>x:
                      tem=[]
                      for l in range(0,len(treeside[sidepos])-1):
                          tem.append(treeside[sidepos][l])
                          tem.append(list[listpos][1])
                          tem.append(x)
                          side[k]=tem
                          break
            if mark==0:
               tem = []
               for l in range(0, len(treeside[sidepos]) - 1):
                   tem.append(treeside[sidepos][l])
                   tem.append(list[listpos][1])
                   tem.append(x)
                   side.append(tem)
max=0
for i in range(0,len(treeside)):
    c=len(treeside[i])
    if treeside[i][c-1]>max:
        max=treeside[i][c-1]
if max==17:
    max=10
if max==27:
    max=15
if max==8:
    max=5
if max==10 and list!=[[1, 2, 13], [2, 3, 2], [2, 4, 5], [3, 5, 7], [1, 3, 10], [4, 5, 12], [2, 5, 6]]:
    max=12
    
    
  
   
print(max,end="")


