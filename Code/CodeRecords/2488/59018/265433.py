import math
a=eval(input())
a.sort()
b=a[len(a)-math.floor(len(a)/2):]
b.sort(reverse=True)
c=a[:len(a)-math.floor(len(a)/2)]
result=[]
for i in range(len(c)):
    result.append(c[i])
    if len(b)>0:        
        result.append(b[i])
        del b[i]
print(result)    
    