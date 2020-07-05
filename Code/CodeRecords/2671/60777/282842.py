case=int(input())
num=0
def count(li,k,i):
    global num
    if(k>(len(li)-i+1)/2):
        return
    if(i==len(li)-1):
        if(k>1):
            return
        else:
            num+=1
            return
    if(i>=len(li)):
        if(k==0):
            num+=1
        return
    if(k==0):
        num+=1
        return
    if(i==0):
        li[0]=1
        li[1]=0
        count(li,k-1,i+2)
        li[0]=0
        li[1]=-1
        count(li,k,i+1)
    else:
        li[i]=1
        li[i+1]=0
        count(li,k-1,i+2)
        li[i]=0
        li[i+1]=-1
        count(li,k,i+1)      

for i in range(case):
    l=int(input())
    c=2**l-1
    for j in range(1,int((l+1)/2+1)):
        num=0
        temp=[-1]*l
        count(temp,j,0)
        c-=num
        
    print(c)