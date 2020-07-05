from itertools import combinations

result=[]
a=list(eval(input()))
b=list(combinations(a,3))
for i in range(len(b)):
    c=sorted(list(b[i]))
    if c[0]+c[1]>c[2]:
        result.append(sum(c))
if len(result)==0:
    print(0)
else:
    print(max(result))