a=input()
map=[]
a=list(input())
a="".join(a[0:len(a)-1])
map.append(eval(a))
a=list(input())
a="".join(a[0:len(a)-1])
map.append(eval(a))
a=list(input())
a="".join(a)
map.append(eval(a))
a=input()
re=[]

def cannotMove(i,j,visited):
    if i<0 or i>2 or j<0 or j>2:
        return True
    if visited[i][j]:
        return True
    return False

def cal(i,j,visited,length):
    visited[i][j]=True
    if cannotMove(i+1,j,visited) and cannotMove(i-1,j,visited) and cannotMove(i,j+1,visited) and cannotMove(i,j-1,visited):
        re.append(length)
    else:
        flag=True
        if i<2 and map[i+1][j]>map[i][j]:
            cal(i+1,j,visited,length+1)
            flag=False
        if i>0 and map[i-1][j]>map[i][j]:
            cal(i-1,j,visited,length+1)
            flag=False
        if j<2 and map[i][j+1]>map[i][j]:
            cal(i,j+1,visited,length+1)
            flag=False
        if j>0 and map[i][j-1]>map[i][j]:
            cal(i,j-1,visited,length+1)
            flag=False
        if flag:
            re.append(length)

for i in range(0,3):
    for j in range(0,3):
        visited=[[False,False,False],[False,False,False],[False,False,False]]
        cal(i,j,visited,1)
print(max(re))