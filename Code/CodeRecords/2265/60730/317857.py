//求无向图的割顶和桥
 
#include<cstdio>
#include<cstring>
#include<vector>
#include<iostream>
#include<cstring>
#include<string>
using namespace std;
const int maxn=1000+10;
int n,m;
int dfs_clock;//时钟，每访问一个节点增1
vector<int> G[maxn];//G[i]表示i节点邻接的所有节点
int pre[maxn];//pre[i]表示i节点被第一次访问到的时间戳,若pre[i]==0表示i还未被访问
int low[maxn];//low[i]表示i节点及其后代能通过反向边连回的最早的祖先的pre值
bool iscut[maxn];//标记i节点是不是一个割点
 
//求出以u为根节点(u在DFS树中的父节点是fa)的树的所有割顶和桥
//初始调用为dfs(root,-1);
int dfs(int u,int fa)  //直接用模板就行了
{
    int lowu=pre[u]=++dfs_clock;
    int child=0;    //子节点数目
    for(int i=0; i<G[u].size(); i++)
    {
        int v=G[u][i];
        if(!pre[v])
        {
            child++;//未访问过的节点才能算是u的孩子
            int lowv=dfs(v,u);
            lowu=min(lowu,lowv);
            if(lowv>=pre[u])
            {
                iscut[u]=true;      //u点是割顶
              /*  if(lowv>pre[u])   //(u,v)边是桥
                    printf("边(%d, %d)是桥\n",u,v);*/
            }
        }
        else if(pre[v]<pre[u] && v!=fa)//v!=fa确保了(u,v)是从u到v的反向边
        {
            lowu=min(lowu,pre[v]);
        }
    }
    if(fa<0 && child==1 )
        iscut[u]=false;//u若是根且孩子数<=1,那u就不是割顶
    return low[u]=lowu;
}
 
int main()
{
    while(scanf("%d",&n)==1&&n)
    {
        dfs_clock=0;
        memset(pre,0,sizeof(pre));
        memset(iscut,0,sizeof(iscut));
        for(int i=1;i<=n;i++) G[i].clear();
        
        int a,b;
         while(scanf("%d",&a)&&a)
        {
            while(getchar()!='\n')
            {
                scanf("%d",&b);
 
               G[a].push_back(b);
                    G[b].push_back(a);
            }
        }
 
 
        dfs(1,-1);
        int ans=0;
        for(int i=1;i<=n;i++)if(iscut[i]==true)
          ans++;
 
          cout<<ans<<endl;
    }
    return 0;
}