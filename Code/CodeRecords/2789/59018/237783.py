k=int(input())
for i in range(k):
    n=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    a.sort(reverse=True)
    b=[]
    for j in range(len(a)):
        m=min(a[j],j+1)
        b.append(m)
    print(max(b))
        
    
   
    
    