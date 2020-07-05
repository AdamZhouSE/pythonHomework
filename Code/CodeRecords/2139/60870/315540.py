#include<bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int maxn=1e5+5;
int head[maxn];
int cnt;
int d[maxn];//记录深度 
int fa[maxn];//父亲 
int anc[maxn][21];//anc数组记录第i个点的2^j的祖先是谁  倍增的思想 
int Min[maxn][21];//记录最小值 
int ans[maxn];
struct node{
    int t;
    int next;
    int id;
}no[maxn];
void add(int u,int v,int id)
{
    no[cnt]={v,head[u],id};
    head[u]=cnt++;
}
void dfs(int x)//dfs倍增求祖先 
{
    for(int i=1;i<=20;i++)//倍增 
        anc[x][i]=anc[anc[x][i-1]][i-1];
    for(int i=head[x];i!=-1;i=no[i].next)
    {
        int v=no[i].t;
        if(v!=anc[x][0])
        {
            anc[v][0]=x;//记录父亲节点 
            fa[v]=no[i].id;//记录那条边
            d[v]=d[x]+1;//更新深度
            dfs(v);
        }
    } 
} 
void Lca(int u,int v,int valu)
{
    if(d[u] < d[v])//一定深度最深的为标准 
        swap(u,v);
    for(int i=20;i>=0;i--)//上推找共同点 
    {
        if(d[anc[u][i]] >= d[v])//找到跟v一样高的或者比v低的点  不断更新u到v之间深度的点 
        {
            Min[u][i]=min(Min[u][i],valu);
            u=anc[u][i];
        }
    }
    if(u==v)//如果v,u在一棵树上 
        return ;
    for(int i=20;i>=0;i--)
    {
        if(anc[u][i] != anc[v][i])//如果不是一个叉子上  还需要往上  找到公共祖先之前一直往上 
        {
            Min[u][i] = min(Min[u][i],valu);
            Min[v][i] = min(Min[v][i],valu);
            u=anc[u][i];
            v=anc[v][i]; 
        }
    }
    Min[u][0] = min(Min[u][0],valu);//无论是否相等都需要更新u v两点 
    Min[v][0] = min(Min[v][0],valu);
} 
int main()
{
    memset(head,-1,sizeof(head));
    memset(Min,INF,sizeof(Min)); 
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<n;i++)
    {
        int u,v;
        scanf("%d%d",&u,&v);
        add(u,v,i);//id标记边号   
        add(v,u,i);	
    }	
    d[1]=1;//深度 
    dfs(1);//倍增 
    for(int i=0;i<m;i++)
    {
        int u,v,Valu;
        scanf("%d%d%d",&u,&v,&Valu);
        Lca(u,v,Valu);//更新min 
    } 
    for(int j=20;j>0;j--)
    {
        for(int i=1;i<=n;i++)
        {
            Min[i][j-1]=min(Min[i][j-1],Min[i][j]);//大区间更新小区间 
            Min[anc[i][j-1]][j-1]=min(Min[anc[i][j-1]][j-1],Min[i][j]);//同上
        }
    }
    for(int i=2;i<=n;i++)//根节点是1  所以从2开始 
        ans[fa[i]]=Min[i][0];
    for(int i=1;i<n;i++)//边是第一个 
    {
        if(ans[i]==INF)
            ans[i]=-1;
        printf("%d\n",ans[i]);
    }
    return 0;
}