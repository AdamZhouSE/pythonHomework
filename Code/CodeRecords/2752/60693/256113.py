def distance(forest,sr,sc,tr,tc):
    row,column = len(forest),len(forest[0])
    queue=[(sr,sc,0)]
    visited={(sr,sc)}
    while queue:
        r,c,d=queue.pop(0)
        if r == tr and c == tc:
            return d
        for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0<=nr<row and 0<=nc<column and (nr,nc) not in visited and forest[nr][nc]:
                visited.add((nr,nc))
                queue.append((nr,nc,d+1))
    return -1

def cut_trees(forest):
    trees = sorted((h,r,c) for r,row in enumerate(forest)
                   for c,h in enumerate(row) if h>1)
    sr = sc = res = 0
    for h,tr,tc in trees:
        d = distance(forest,sr,sc,tr,tc)
        if d < 0:
            return -1
        res += d
        sr,sc = tr,tc

    return res

forest=[]
input()
inp=input()
while inp!=']':
    if inp[-1]==',':forest.append(eval(inp[:-1]))
    else:forest.append(eval(inp))
    inp = input()
    
print(cut_trees(forest))