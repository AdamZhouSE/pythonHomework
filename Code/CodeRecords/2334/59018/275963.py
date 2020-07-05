from itertools import combinations

result=[]
a=list(eval(input()))
b=list(combinations(a,3))
for i in range(len(b)):
    b[i].sort()
    if b[i][0]+b[i][1]>b[i][2]:
        result.append(sum(b[i]))
print(max(result))        
        

    
    
