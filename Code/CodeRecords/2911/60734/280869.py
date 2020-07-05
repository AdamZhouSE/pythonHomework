def find(x):
    if s[x]<0:
        return x
    else:
        return find(s[x])

lst = list(map(int,input().split(' ')))
n,m = lst[0],lst[1]
golds = list(map(int,input().split(' ')))
golds.insert(0,-1)
relation = []
for i in range(m):
    relation.append(list(map(int,input().split(' '))))

s = [-1]*(n+1)
for re in relation:
    root1 = find(re[0])
    root2 = find(re[1])
    if s[root2]<s[root1]:
        s[root1] = root2
        golds[root2] = min(golds[root1],golds[root2])
    else:
        if s[root1] == s[root2]:
            s[root1]-=1
        s[root2] = root1
        golds[root1] = min(golds[root1],golds[root2])
roots = [i for i in range(1,len(s)) if s[i]<0]
print(sum([golds[i] for i in roots]))