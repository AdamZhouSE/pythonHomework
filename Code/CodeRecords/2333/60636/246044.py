x=int(input())
y=int(input())
bound=int(input())
res=[]
for i in range(1,bound+1):
    while(i>0):
        if(i%y==0):
            res.append(i)
            break
        else:
            i=i-x
print(res)