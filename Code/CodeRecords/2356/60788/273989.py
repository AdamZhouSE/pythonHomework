num=int(input().strip())
for i in range(num):
    length=num=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    flag=True
    for k in range(1,len(s)-1):    
        if s[k]>=max(s[:k]) and s[k]<=min(s[k+1:]):            
            print(s[k])
            flag=False
            break
    if flag:
        
        print(-1)