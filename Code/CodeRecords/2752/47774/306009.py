from collections import deque, namedtuple
t=input()
matrix=[]
while(1):
    try:
        a=input().replace(',',' ').strip().replace('[','').replace(']','').split(' ')    
        if a!=['']:
            matrix.append(a)
    except:
        break
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j]=int(matrix[i][j])

M=len(matrix)
N=len(matrix[0])
lst=[]
for i in range(M):
    for j in range(N):
        c=matrix[i][j]
        if c>1:
            lst.append(c)
lst=sorted(lst)
nt=len(lst)
visited=[[-2 for i in range(N)] for j in range(M)]
q=deque()
TreeNode = namedtuple('TreeNode', ['row','col','id'])
if lst[0]==matrix[0][0]:
    q.append(TreeNode(0,0,0))
    visited[0][0]=0
else:
    q.append(TreeNode(0,0,-1))
dirs=[(0,-1),(0,1),(1,0),(-1,0)]
def solve():
    step=0
    while q:
        nq=len(q)
        while nq:
            nq=nq-1
            node=q.popleft()
            if node.id==nt-1:
                return step
            for d in dirs:
                row=node.row+d[0]
                col=node.col+d[1]
                col_id=node.id
                if row<0 or row>=M or col<0 or col>=N:
                    continue
                c=matrix[row][col]
                if c==0:
                    continue
                if c>1 and lst.index(c)==node.id+1:
                    cur_id=node.id+1
                if visited[row][col]>=cur_id:
                    continue
                visited[row][col]=cur_id
                q.append(TreeNode(row,col,cur_id))
        step=step+1
    return -1
print(solve())
    
    
    
        