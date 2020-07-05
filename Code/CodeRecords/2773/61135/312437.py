def DFS(numlist,i,j):
    a=0;
    movedirs=[[0,1],[1,0],[0,-1],[-1,0]]
    for k in movedirs:
        x=i+k[0]
        y=j+k[1]
        if(0 <= x and x < len(numlist) and 0 <= y and y < len(numlist[0]) and numlist[x][y] > numlist[i][j]):
            a=max(a,DFS(numlist,x,y))
    return a+1
numstr=""
temp=""
while(temp!="]"):
    numstr+=temp
    temp=input()
numstr+="]"
numlist=eval(numstr)
longest=0
for i in range(0,len(numlist)):
    for j in range(0,len(numlist[0])):
        longest=max(longest,DFS(numlist,i,j))
print(longest)