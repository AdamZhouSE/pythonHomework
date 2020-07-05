matrix=[]
try:
    while True:
        inp=input()
        if inp!="[" and inp!="]":
            if inp[-1]==",":
                inp=inp[:-1]
            matrix.append(eval(inp))
except EOFError:
    pass
def dfs(row,col,matrix,start,used):
    if row>=len(matrix) or col>=len(matrix[0]) or matrix[row][col]<=start:
        return 1
    temp=row*col-1
    if temp in used:
        return 1
    else:
        start=matrix[row][col]
        used.append(temp)
        longest=max(dfs(row+1,col,matrix,start,used)+1,
                   dfs(row-1,col,matrix,start,used)+1,
                   dfs(row,col+1,matrix,start,used)+1,
                   dfs(row,col-1,matrix,start,used)+1)
        used.pop()
        return longest
final=0
width=len(matrix[0])
end=width*len(matrix)-1
for i in range(end):
    row=i//width
    col=i%width
    start=matrix[row][col]
    temp=dfs(row,col,matrix,start-1,[])
    final=max(temp,final)
print(final)

