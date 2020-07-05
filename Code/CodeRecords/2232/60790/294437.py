#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define LL long long
#define mod 100000000
#define inf 0x3f3f3f3f
#define eps 1e-6
#define N 110
#define FILL(a,b) (memset(a,b,sizeof(a)))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define PII pair<int,int>
using namespace std;
struct edge
{
    int v,next;
    edge(){}
    edge(int v,int next):v(v),next(next){}
}e[N*N];
int n,scc,step,top,tot;
int head[N],dfn[N],low[N],belong[N],Stack[N];
int in[N],out[N];
bool instack[N];
void init()
{
    tot=0;step=0;scc=0;top=0;
    FILL(head,-1);FILL(dfn,0);
    FILL(low,0);FILL(instack,false);
    FILL(in,0);FILL(out,0);
}
void addedge(int u,int v)
{
    e[tot]=edge(v,head[u]);
    head[u]=tot++;
}
void tarjan(int u)
{
    int v;
    dfn[u]=low[u]=++step;
    Stack[top++]=u;
    instack[u]=true;
    for(int i=head[u];~i;i=e[i].next)
    {
        v=e[i].v;
        if(!dfn[v])
        {
            tarjan(v);
            low[u]=min(low[u],low[v]);
        }
        else if(instack[v])
        {
            low[u]=min(low[u],dfn[v]);
        }
    }
    if(dfn[u]==low[u])
    {
        scc++;
        do
        {
            v=Stack[--top];
            instack[v]=false;
            belong[v]=scc;
        }while(v!=u);
    }
}
void solve()
{
    for(int i=1;i<=n;i++)
        if(!dfn[i])tarjan(i);
    if(scc==1)
    {
        printf("1\n0\n");
        return;
    }
    for(int u=1;u<=n;u++)
    {
        for(int i=head[u];~i;i=e[i].next)
        {
            int v=e[i].v;
            if(belong[v]!=belong[u])
            {
                out[belong[u]]++;
                in[belong[v]]++;
            }
        }
    }
    int a=0,b=0;
    for(int i=1;i<=scc;i++)
    {
        if(!in[i])a++;
        if(!out[i])b++;
    }
    printf("%d\n%d\n",a,max(a,b));
}
int main()
{
    int u;
    while(scanf("%d",&n)>0)
    {
        init();
        for(int i=1;i<=n;i++)
        {
            while(scanf("%d",&u)&&u)
                addedge(i,u);
        }
        solve();
    }
}