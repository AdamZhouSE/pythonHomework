arr=list(map(int,input().split(','))
dd=int(input())
d={}
for a in arr:
    d[a]=d.get(a-dd,0)+1
print(max(d.values()))