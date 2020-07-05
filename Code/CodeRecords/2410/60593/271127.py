arr=list(map,input().split(','))
dif=int(input())
d={}
for a in arr:
    d[a]=d.get(a-dif,0)+1
print(max(d.values()))