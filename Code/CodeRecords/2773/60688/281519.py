numstr="";
temp="";
while(temp!="]"):
    numstr+=temp;
    temp=input();
numstr+="]"
numlist=eval(numstr);
# print(numlist)
#暴力调用：
def dfs(numlist:list,i,j):
    thislongest=0;
    for k in movedirs:
        x=i+k[0]
        y=j+k[1];
        if(0 <= x and x < m and 0 <= y and y < n and numlist[x][y] > numlist[i][j]):
            thislongest=max(thislongest,dfs(numlist,x,y));#筛选功能，只有当确定是增序列才进行进一步深度
    return thislongest+1;#因为本身也是1个//相当于递归到底，然后返回计数。
m=len(numlist)
n=len(numlist[0]);
movedirs=[[0,1],[1,0],[0,-1],[-1,0]];#遍历临接元素用这种遍历+预定义方式搞定
longest=0;
for i in range(m):
    for j in range(n):
        longest=max(longest,dfs(numlist,i,j));
print(longest)