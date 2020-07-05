n=input()
l=list(map(int,input().split()))
c=0
m=0

for i in range(1,len(l)):

    if l[i-1]*2 >= l[i]:
        c=c+1

    else:
        c=0

    if c>m:
        m=c    
    
print (m+1)
