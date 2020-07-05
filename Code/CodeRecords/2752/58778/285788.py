from collections import deque
matrix=[]
t=0
while(t<4):
    try:
        s=input()
    except EOFError:
        break
    if(s!='[' and s!=']'):
        if(s[len(s)-1]==','):
            s=s[1:len(s)-1]
        else:
            s=s[1:]
        matrix.append(eval(s))
    t=t+1

def dist(matrix,sr,sc,tr,tc):
    R,C=len(matrix),len(matrix[0])
    #使用队列来进行bfs，初始队列为源位置
    queue=deque([(sr,sc,0)])
    #用来表示有没有查看过
    seen={(sr,sc)}
    while queue:
        r,c,d=queue.popleft()
        if r==tr and c==tc:
            #如果当前位置就是目标
            return d
        for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if(0<=nr<R and 0<=nc<C and (nr,nc) not in seen and matrix[nr][nc]):
                seen.add((nr,nc))
                #将这个节点加入到待处理的节点
                queue.append((nr,nc,d+1))
    return -1
def cutTree(matrix):
    #将所有的树按照高度从低到高排序，表示要走过的路径
    trees = sorted((v, r, c) for r, row in enumerate(matrix)
                   for c, v in enumerate(row) if v > 1)
    #开始时的源位置为（0,0）
    sr=sc=ans=0
    #根据已经排好序的列表来走
    for v,tr,tc in trees:
        d=dist(matrix,sr,sc,tr,tc)
        if(d<0):
            return -1
        ans+=d
        sr,sc=tr,tc
    return ans

print(cutTree(matrix))