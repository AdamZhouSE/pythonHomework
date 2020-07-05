list=input().split(',')
k=int(input())
res=[]
for i in range(2,len(list)+1):
    for j in range(len(list)-i+1):
        temp=[]
        for k in range(j,j+i):
            temp.append(list[k])
        res.append(temp)
c=0
for i in range(len(res)):
    all=0
    for j in range(len(res[i])):
        all+=int(res[i][j])
    if all%k==0:
        c=1
if c==1:
    print('True')
else:
    print('False')