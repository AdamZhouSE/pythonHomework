list=input().split(',')
res=[]
if len(list)<3:
    print(0)
else:
    for i in range(3,len(list)+1):
        for j in range(len(list)-i+1):
            temp=[]
            for k in range(j,j+i):
                temp.append(list[k])
            res.append(temp)
    def panduan(list):
        a=int(list[1])-int(list[0])
        for i in range(len(list)-1):
            if a!=int(list[i+1])-int(list[i]):
                return False
        return True
    count=0
    for i in range(len(res)):
        if panduan(res[i]):
            count+=1
    print(count)