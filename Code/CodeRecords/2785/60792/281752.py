def dfs(x,y,n,list1):
    if x==n:
        return y%360==0
    if dfs(x+1,y+list1[x],n,list1):
        return True
    if dfs(x+1,y-list1[x],n,list1):
        return True
    return False

num=int(input())
list1=[]
for i in range(0,num):
    list1.append(int(input()))
if(dfs(0,0,num,list1)):
    print("YES")
else:
    print("NO")