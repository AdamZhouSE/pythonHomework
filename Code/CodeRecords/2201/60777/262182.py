t=int(input())
def prime(x):
    if(x==1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

for i in range(t):
    temp=[int(x) for x in input().split()]
    add=sum(temp)
    add+=1
    while(not prime(add)):
        add+=1
    print(add-sum(temp))