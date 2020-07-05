#include<stdio.h>
#include<cstring>
#include<algorithm>
#define ll long long
#define Min(x,y) ((x<y)?(x):(y))
#define Max(x,y) ((x>y)?(x):(y))
#define MAXM 10005
#define MAXN 10005
using namespace std;

int N,T,P,mark[MAXN],Ans_cnt;
ll Ans_tot;

int tot,en[MAXM],nex[MAXM],las[MAXN];
void ADD(int x,int y)
{
    en[++tot]=y;
    nex[tot]=las[x];
    las[x]=tot;
}

int pbc,VT,dfn[MAXN],low[MAXN],be[MAXN];
bool Cut[MAXN];
void Tarjan(int x,int f)
{
    dfn[x]=low[x]=++VT;

    int i,y,son=0;

    for(i=las[x];i;i=nex[i])
    {
        y=en[i];
        if(!dfn[y])
        {
            Tarjan(y,x);
            son++;
            low[x]=Min(low[x],low[y]);
            if(low[y]>=dfn[x]&&f)Cut[x]=true;
        }
        else if(y!=f)low[x]=Min(low[x],dfn[y]);
    }
    if(f==0&&son>=2)Cut[x]=true;
}

bool vis[MAXN];
int con[MAXN],Size[MAXN],CTime[MAXN];
//con记录与该点双连通分量连接的节点数，CTime名字起得略差，用来标记割点是否已经被当前的点双连通分量讨论过
void DFS(int x)
{
    int i,y;
    vis[x]=true;Size[pbc]++;
    for(i=las[x];i;i=nex[i])
    {
        y=en[i];
        if(vis[y]||Cut[y])
        {
            if(Cut[y]&&CTime[y]!=pbc)con[pbc]++,CTime[y]=pbc;
            continue;
        }
        DFS(y);
    }
}

void init()
{
    T++;VT=tot=P=pbc=Ans_cnt=0;
    Ans_tot=1;

    memset(las,0,sizeof(las));
    memset(dfn,0,sizeof(dfn));
    memset(low,0,sizeof(low));
    memset(Cut,false,sizeof(Cut));
    memset(mark,false,sizeof(mark));
    memset(vis,false,sizeof(vis));
    memset(be,0,sizeof(be));
    memset(Size,0,sizeof(Size));
    memset(con,0,sizeof(con));
    memset(CTime,0,sizeof(CTime));
}

int main()
{
    int i,x,y;

    scanf("%d",&N);

    while(N)
    {
        init();

        for(i=1;i<=N;i++)
        {
            scanf("%d%d",&x,&y);
            ADD(x,y);ADD(y,x);
            P=Max(P,x);P=Max(P,y);
            mark[x]=mark[y]=true;
        }

        for(i=1;i<=P;i++)if(!dfn[i])Tarjan(i,0);
        for(i=1;i<=P;i++)if(mark[i]&&(!vis[i])&&(!Cut[i]))pbc++,DFS(i);

        for(i=1;i<=pbc;i++)
        {
            if(con[i]==0)Ans_tot*=1ll*(Size[i]-1)*Size[i]/2,Ans_cnt+=2;
            else if(con[i]==1)Ans_tot*=Size[i],Ans_cnt++;
        }

        printf("Case %d: %d %lld\n",T,Ans_cnt,Ans_tot);

        scanf("%d",&N);
    }
}