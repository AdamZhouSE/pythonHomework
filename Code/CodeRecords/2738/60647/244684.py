list=[]
input()
for i in range(4):
    str=input()
    temp=[]
    for j in str:
        if j=="1"or j=="0":
            temp.append(j)
    list.append(temp)
res=0
for i in range(len(list)):
    for j in range(len(list[0])):
        wide=0
        height=0
        if int(list[i][j])==1:
            size=0
            for m in range(j,len(list[0])):
                if int(list[i][m])==1:
                    wide+=1#宽加一
                else:
                    break
            for n in range(i,len(list)-1):
                count=0
                for k in range(j,j+wide):
                    if int(list[n][k])!=1:
                        count=1
                        break
                if count==0:
                    height+=1
                else:
                    break
            size=wide*height
            if size>=res:
                res=size
print(res)#求最大矩形