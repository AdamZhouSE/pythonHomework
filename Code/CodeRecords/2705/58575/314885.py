import collections

edges=[]
temp=input()[1:-1]

i=0
while(i<len(temp)):
    i=temp.index("[")
    j=temp.index("]")
    tmp=temp[i+1:j]
    tmp=list(map(int,tmp.split(",")))
    edges.append(tmp)
    temp=temp[j+1:]
    i=j

outs = [edge[1] for edge in edges]
count = collections.Counter(outs)
for key in count.keys():
    if count[key] == 2:
        redundance = [edge for edge in edges if edge[1] == key]
        edges = [edge for edge in edges if edge[1] != key] + redundance
        break

dic = {}
n = len(edges)

def find(p):
    while p != dic[p]:
        p = dic[p]
    return p


def union(p, q):
    root1, root2 = find(p), find(q)
    if root1 == root2:
        return True
    else:
        dic[root1] = root2
        return False


for i in range(1, n + 1):
    dic[i] = i
for edge in edges:
    if union(edge[0], edge[1]):
        print(edge)
