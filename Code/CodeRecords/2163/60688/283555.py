def factorial(num):
    res = [1];
    i = 1;
    while i <= num:
        res.append(i * res[i - 1]);
        i += 1;
    return res;

# visited:判断某位数是否被使用（相当于记录）
# level 递归层数：最顶层是0 ，n源，k目标，
# res 记录
# !!!回溯visited的必要性：：：因为不同于图：每个节点的邻居与上层节点没关系
# 回溯or通用型深度优先搜索：：每层选择对象都是一列，并且上层选择后，下层自然不能选，，自然need visited传递
def DFS(visited, level, n, k, res):
    if(level==n):#退出条件
        return res;
    curr=factoriallist[n-1-level];
    for i in range(1,n+1):
        if visited[i]==1:
            continue;
        if curr<k:#时刻搞清楚curr是啥：是当前层数本轮选择概括的选项，
            k-=curr#这里是剪枝！！只有当符合迭代条件，才会进入深层迭代
            continue#减掉当前枝叶进入下个情况
        if(curr>=k):
            res+=str(i)#找到了本层该进入（向下搜索）的点
            visited[i]=1;#已经选择
            return DFS(visited,level+1,n,k,res);
n = int(input())
k = int(input())
factoriallist=factorial(n);
visited = [0 for _ in range(n + 1)]
# print(visited)
res = ""
if n == 0:
    res = "";
else:
    res=DFS(visited,0,n,k,"");
print(res);