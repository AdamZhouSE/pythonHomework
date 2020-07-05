from itertools import combinations
numb=int(input())
sources=[]
for i in range(numb):
    x=input().split(",")
    source=[]
    source.append(int(x[0]))
    source.append(int(x[1]))
    sources.append(source)
target=list(combinations(sources,3))
ss=[]
for i in target:
    s=((i[0][0]*i[1][1]-i[1][0]*i[0][1])+(i[1][0]*i[2][1]-i[2][0]*i[1][1])+(i[2][0]*i[0][1]-i[0][0]*i[2][1]))
    ss.append(s)
print(max(ss))