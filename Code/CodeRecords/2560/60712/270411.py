from collections import Counter
n = int (input())
for i in range(n):
    x=int(input())
    l = list(map(int,input().split()))
    m = int(input())
    c=Counter(l)
    l2=c.most_common()[::-1]
    s = 0
    for j in range(len(l2)):
        m=m-l[0][1]
        if m>=0:
            s+=1
        else:
            break
    print(len(l2)-s)
            
            
    
    
    
             