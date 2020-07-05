t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    k=int(input())
    result=0        
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(s[i])>int(s[j]):
                s[i],s[j]=s[j],s[i]
    for a in range(0,n-3):
        if result==1:
            break
        for b in range(a+1,n-2):
            if result==1:
                break
            for c in range(b+1,n-1):
                if result==1:
                    break
                for d in range(c+1,n):
                    if int(s[a])+int(s[b])+int(s[c])+int(s[d])==k:
                        result=1
                        break
                    
    print(result)        