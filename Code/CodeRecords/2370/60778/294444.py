target=int(input())
res=[1]
i=1
while(i<target):
    i*=4
    res+=[0,0]
p=0
n=i
while(True):
    if(target==n):
        break
    else:
        p+=1
        i/=2
        if(n>target and p%2==1):
            n-=i
            res[p]=1
        elif(n<target and p%2==0):
            n+=i
            res[p]=1
print("".join(list(map(str,res))))