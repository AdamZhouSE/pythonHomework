inp=input()
length=len(inp)
list=[]
i=0
while i<=length-1:
    temp=[]
    while i<=length-1:
        if inp[i].isdigit():
            temp.append(int(inp[i]))
        elif inp[i]==']':
            break;
        i+=1
    i+=1
    if(len(temp)!=0):
        list.append(temp)
width=len(list[0])
height=len(list)
startx=height-1
starty=0
while (startx==0 and starty==width-1)==False:
    tempx=startx
    tempy=starty
    list_temp=[]
    while startx<=height-1 and starty <= width-1 and startx>=0:
        list_temp.append(list[startx][starty])
        startx+=1
        starty+=1
    list_temp.sort()
    startx=tempx
    starty=tempy
    k=0
    while startx <= height - 1 and starty <= width - 1:
        list[startx][starty]=list_temp[k]
        k+=1
        startx += 1
        starty += 1
    startx = tempx
    starty = tempy
    if startx!=0:
        startx-=1
        starty=0
    else:
        starty+=1
print(list)