case=int(input())

def score(e1,e2):
    res=0
    while(e2!=1):
        if(e1%e2==0):
            e1-=1
            res+=1
        else:
            e2-=1
    return res

for i in range(case):
    temp=[int(x) for x in input().split(' ')]
    x=temp[0]
    y=temp[1]
    z=temp[2]
    
    print(score(x,z),end=' ')
    print(score(y,z))