#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<stack>

using namespace std;

const int INF=23333333;
const int maxn=233333;
int head[maxn],nxt[maxn],to[maxn];
int ff[maxn],tt[maxn];
int scc[maxn],low[maxn],dfn[maxn],rd[maxn],xh[maxn];
int cost[maxn],minc[maxn];
int cnt=0,dfs_clock=0,ans=0;
int tot;
int n,p;
int r;
stack<int>s;

void addedge(int f,int t)
{
    to[++tot]=t;
    nxt[tot]=head[f];
    head[f]=tot;
}

void find_scc(int u)
{
    dfn[u]=low[u]=++dfs_clock;
    s.push(u);
    for(int i=head[u];i;i=nxt[i])
    {
        int v=to[i];
        if(!dfn[v])
        {
            find_scc(v);
            low[u]=min(low[u],low[v]);  
        }
        else if(!scc[v])
        {
            low[u]=min(low[u],dfn[v]);
        }
    }
    if(low[u]==dfn[u])
    {
        cnt++;
        xh[cnt]=u;
        while(1)
        {
            int x=s.top();
            s.pop();
            scc[x]=cnt;
            minc[cnt]=min(minc[cnt],cost[x]);
            xh[cnt]=min(xh[cnt],x);
            if(x==u)
            break;
        }
    }
}

int main()
{
    cin>>n>>p;
    for(int i=1;i<=n;i++) cost[i]=INF; 
    for(int i=1;i<=p;i++)
    {
        int a,b;
        cin>>a>>b;
        cost[a]=b;
    }
    cin>>r;
    for(int i=1;i<=r;i++)
    {
        cin>>ff[i]>>tt[i];
        addedge(ff[i],tt[i]);
    }
    for(int i=1;i<=n;i++) minc[i]=INF; 
    for(int i=1;i<=n;i++)
    {
        if(!dfn[i])
        find_scc(i);
    }
    for(int i=1;i<=r;i++)
    {
        if(scc[ff[i]]!=scc[tt[i]])
        rd[scc[tt[i]]]++;
    }
    bool pd=1;
    int noans=INF,yesans=0;
    for(int i=1;i<=cnt;i++)
    {
        if(!rd[i])
        {
            if(minc[i]==INF)
            {
                pd=0;
                noans=min(noans,xh[i]);
            }
            else yesans+=minc[i];
        }
    }
    if(pd)
    {
        cout<<"YES"<<endl;
        cout<<yesans<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
        cout<<noans<<endl;
    }
    return 0;
}
