import collections
def removeStones(stones):
    p = collections.defaultdict(set)
    for x, _y in stones:
        y = _y + 10000
        p[x] |= {x}  
        p[y] |= {y}
        if p[x] != p[y]:  
            p[x] |= p[y]  
            for z in p[y]:
                p[z] = p[x] 
    return len(stones) - len(set(id(c) for c in p.values()))
arr=eval(input())
print(removeStones(arr))