temp=[int(x) for x in input().split(',')]
res=[0]*2

for i in range(1,len(temp)+1):
    if(not(i in temp)):
        res[1]=i
    elif(temp.count(i)>1):
        res[0]=i
        
print(res)