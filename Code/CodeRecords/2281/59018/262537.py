def leader(a):
    b=[]
    for j in range(len(a)-1):
        for k in range(j,len(a)):
            if a[j]<a[k]:
                break
        else:        
            b.append(a[j])
    b.append(a[-1])
    return b
            
        



T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    print(type(leader(a)))
    
    