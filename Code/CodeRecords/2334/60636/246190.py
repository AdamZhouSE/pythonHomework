from itertools import combinations
lists=input().split(",")
sources=[]
for i in lists:
    sources.append(int(i))
target=list(combinations(sources,3))
c=[]
for i in target:
    sum=int((i[0]+i[1]+i[2])/2)
    if(sum*(sum-i[0])*(sum-i[1])*(sum-i[2])>0):
        c.append(2*sum)
    else:
        c.append(-1)
if(max(c)!=-1):
    print(max(c))
else:
    print(0)