#include<bits/stdc++.h>
using namespace std;
struct node
{
    int next,to;
}tree[100000];  //存图，蒟蒻不会stl
int n,a[100000],head[100000],cnt,f[100000],ans; //f[u] 表示以u为根且包含u的最大权联通块
void add(int x,int y) 
{
    tree[++cnt].next=head[x];
    tree[cnt].to=y;
    head[x]=cnt;
}
void dfs(int u,int fa)//u为当前节点,fa为u的爸爸
{
    f[u]=a[u];  //先给f[u]赋初值，就是u本身的美观指数
    for(int i=head[u];i;i=tree[i].next) //找儿子
    {
        int v=tree[i].to;  
        if(v!=fa)  //之前加的双向边，可能跑回去
        {
            dfs(v,u);  //继续向下找
            f[u]+=max(0,f[v]);  //状态转移
        }
    }
    ans=max(ans,f[u]); //更新ans
}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for(int i=1,x,y;i<n;i++)
    {
        scanf("%d%d",&x,&y);
        add(x,y);add(y,x);  //注意加双向边
    }
    dfs(1,0);  
    printf("%d",ans);
}