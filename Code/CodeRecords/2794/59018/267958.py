def findbooks(n,a,q):
    sums=[]
    first=1
    last=a[0]   
    for j in range(n):
        sums.append((first,last))
        first=1+a[j]
        last=sum(a[0:j+2])
    for k in range(n):
        if sums[k][0]<=q<=sums[k][1]:
            print(k+1)
            break
    
    
    
    
    
    
    
    


n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
m=int(input())
inf=input().split(' ')
b=[int(y) for y in inf]
for q in b:
    findbooks(n,a,q)
    
    
    
    
    
    