from collections import Counter
n = int(input())
for i in range(n):
    sumOfStr = int(input())
    l = input().split()
    l2 = ['0'] * sumOfStr
    for j in range(sumOfStr):
        s=list(l[j])
        s.sort()
        l2[j] = ''.join(s)
    c=Counter(l2)
    c=c.items()
    output=sorted(c,key=lambda x :x[1])
    result=""
    for j in range(len(output)):
        result+=str(output[j][1])
    print(*result)
        
    
        


