
def tobinary(x):
    tmp=1
    exp=0
    for i in range(100):
        if x>=tmp:
            tmp*=2
            exp+=1
        else:
            exp-=1
            break
    j=1
    res=''
    for i in range(exp):
        j*=2
    #print(x)
    
    #print(exp)
    #print(j)
    for i in range(exp+1):
        res+=str(int((x//j)))
        x-=j*(x//j)
        j/=2
    return res
n=int(input())
for j in range(n):
    t=int(input())
    for i in range(1,t+1):
        print(tobinary(i),end=" ")
    
    
    print()
    