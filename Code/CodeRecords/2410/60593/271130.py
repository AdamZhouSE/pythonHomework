arr=list(map(int,input().split(','))
diff=int(input())
d={}
for a in arr:
    d[a]=d.get(a-diff,0)+1
print(max(d.values()))