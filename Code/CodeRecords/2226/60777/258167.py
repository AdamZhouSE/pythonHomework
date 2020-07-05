left=int(input())
right=int(input())
res=[]
for i in range(left,right+1):
    selfdig=True
    temp=str(i)
    if(i<=9):
        res.append(i)
    elif('0' not in temp):
        for j in range(len(temp)):
            dig=int(temp[j])
            if(not(i%dig==0)):
                selfdig=False
        if(selfdig):
            res.append(i)
            
print(res)