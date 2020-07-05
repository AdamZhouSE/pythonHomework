n=int(input())
a={}
b=[]
for i in range(n):
    name,score=input().split()
    score=int(score)
    a[name]=a.get(name,0)+score
    b.append([a[name],name])
    m = max(a.values())
for score,name in b:
    if score>=m:
        print(name)
        break