x=int(input())
y=int(input())
res=0
if(x>=y):
    res=x-y
elif(x<y):
    while(x<y):
        y=(y/2) if (y%2==0) else (y+1)
        res+=1
    res=res+x-y
print(int(res))