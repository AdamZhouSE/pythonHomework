t=int(input())

def pr(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    if(x==1):
        return False
    else:
        return True

def prime(x):
    temp=str(bin(x))
    count=0
    for i in range(len(temp)):
        if(temp[i]=='1'):
            count+=1
    if(pr(count)):
        return True
    else:
        return False
    
for i in range(t):
    temp=[int(x) for x in input().split()]
    count=0
    for j in range(temp[0],temp[1]+1):
        if(prime(j)):
            count+=1
    print(count)
            
     