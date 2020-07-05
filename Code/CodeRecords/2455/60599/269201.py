#include <bits/stdc++.h>

using namespace std;
#define inf 0x3f3f3f3f
int flower[16600],n,next[40010],pre[40010],last[40010],f[16600],num=0;
/*
flower[i]表示第i个节点的值
next[i]表示编号为i的边的下一个节点的值
pre[i]表示编号为i的边的上一个节点相连的边的编号
last[i]表示与第i个节点相连的最后一条边的编号（因为与i节点相连的边可能不止一条）
last[i]也可以理解成许多节点用边相连形成一条串，第i条边在这个串中的上一条边就是last[i]
f[i]表示第i节点的子树的最大和
*/
bool vis[16600];//标记每个节点是否访问过
int ans=-inf;
void cnct(int x,int y)
{
    num++;//边的编号++
    next[num]=y;//第num条边的下一个节点是y
    pre[num]=last[x];//第num条边的上一条边是x的上一条边
    last[x]=num;//现在x的上一条边是num了
}
int dfs (int u)
{
    int sum=0;
    if(f[u])
    return f[u];
    int i=last[u];//u节点的上一条边
while(i)//如果有这条边
 {
        int nxt=next[i];//nxt就是此边相连的另一个节点（这条边把u与nxt相连）
        if(!vis[nxt])
        {
            vis[nxt]=1;
            int x=dfs(nxt);//往上找串
            if(x>0) sum+=x;//找完后如果子树权值和>0，加上
        }
        i=pre[i];//再找i的前一个边
    }
    f[u]=sum+flower[u];
    if(f[u]>ans) ans=f[u];
    return f[u];
}
int main()
{
    memset(flower,0,sizeof flower);
    memset(pre,0,sizeof pre);
    memset(last,0,sizeof last);
    memset(next,0,sizeof next);
    memset(f,0,sizeof f);
    memset(vis,false,sizeof vis);
    //freopen("de.txt","r",stdin);
    scanf("%d",&n);
    for (int i=1;i<=n;++i)
    scanf("%d",&flower[i]);
    for (int i=1;i<n;++i)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        cnct(x,y);//将两个节点连接起来
        cnct(y,x);//双向都要连接
    }
    vis[1]=1;
    dfs(1);
    printf("%d",ans);
    return 0;
}