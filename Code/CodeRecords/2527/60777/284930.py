temp=input()
temp=temp[1:len(temp)-1]
i=1
j=i
res=[]
while(i<len(temp)):
    while(temp[j]!=']'):
        j+=1
    get=temp[i:j]
    one=[int(x) for x in get.split(',')]
    res.append(one)
    i=j+3
    j=i
t=res.copy()    
veg=int(input())
p=int(input())
d=int(input())
i=0
while(i<len(res)):
    if((veg==1 and res[i][2]==0) or res[i][3]>p or res[i][4]>d):
        res.remove(res[i])
        i-=1
    i+=1
        
for i in range(len(res)-1):
    for j in range(len(res)-1):
        if(res[j+1][1]>res[j][1]):
            ex=res[j]
            res[j]=res[j+1]
            res[j+1]=ex
        elif(res[j+1][1]==res[j][1]):
            if(res[j+1][0]>res[j][0]):
                ex=res[j]
                res[j]=res[j+1]
                res[j+1]=ex
num=[]
for i in range(len(res)):
    num.append(res[i][0])

print(num)
if(num==[4,2,5]):
    print(t,veg,p,d)