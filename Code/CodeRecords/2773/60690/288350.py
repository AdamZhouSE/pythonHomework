str=input()
list=[]
while str!="]":
    if str!="[": list.append(str)
    str=input()
for i in range(len(list)):
    if i!=len(list)-1:
        list[i]=list[i][3:-2].split(",")
    else:
        list[i]=list[i][3:-1].split(",")
    for j in range(len(list[i])):
        list[i][j]=int(list[i][j])

def depSearch(list,roads,length,x,y,indexs):
    if len(indexs)==len(list)*len(list[0]):
        roads.append(len(indexs))
        return
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (i==x and j==y) or (i==x-1 and j==y-1) or (i==x+1 and j==y+1) or (i==x+1 and j==y-1) or(i==x-1 and j==y+1) : continue
            else:
                if i>=0 and j>=0 and i<len(list) and j<len(list[0]):
                    if list[i][j]>list[x][y] and [i,j] not in indexs:
                        indexs.append([i,j])
                        depSearch(list,roads,length+1,i,j,indexs)
                    else:
                
                        roads.append(length)


roads=[]
for i in range(len(list)):
    for j in range(len(list[0])):
        indexs=[[i,j]]
        depSearch(list,roads,1,i,j,indexs)
print(max(roads))