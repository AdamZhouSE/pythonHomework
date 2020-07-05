from collections import defaultdict


def smallest_str(string,pairs):
    p=list(range(len(string)))

    def find(x):
        if x != p[x]:
            p[x]=find(p[x])
        return p[x]

    for i,j in pairs:
        px,py=find(i),find(j)
        if px != py:
            p[px]=py

    tmp=defaultdict(list)
    for i,v in enumerate(p):
        tmp[find(v)].append(string[i])
    for k in tmp:
        tmp[k].sort(reverse=True)

    res=[]
    for i in range(len(string)):
        res.append(tmp[find(i)].pop())
    return ''.join(res)

string=input()
pairs=eval(input())
print(smallest_str(string,pairs))