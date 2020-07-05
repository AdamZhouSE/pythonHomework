#include<algorithm>
#include<iostream>
#include<complex>
#include<cstring>
#include<string>
#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#define N 100039
#define mod 20070831
#define inf 0x3f3f3f3f
#define ll unsigned long long
using namespace std;
struct edge
{
    int to,next;
}net[N<<1];
struct poi
{
    int n;
    ll w,suf;
    bool friend operator < (poi a,poi b)
    {
        return a.w<b.w;
    }
};
int n,tot,head[N],siz[N],deg[N];
ll bs[N],hs[N];
vector<poi> son[N];
map<ll,int> mp;
void add(int u,int v)
{
    net[++tot]=(edge){v,head[u]},head[u]=tot,deg[u]++;
    net[++tot]=(edge){u,head[v]},head[v]=tot,deg[v]++;
}
void get_base(ll base,int lim)
{
    bs[0]=1;
    for(int a=1;a<=lim;a++)
    {
        bs[a]=bs[a-1]*base;
    }
}
void calc_hash(int pos,int sz)
{
    sort(son[pos].begin(),son[pos].end());
    hs[pos]=0;
    for(int a=0,b=son[pos].size();a<b;a++)
    {
        hs[pos]+=bs[a+1]*son[pos][a].w;
    }
    hs[pos]+=sz;
}
void dfs(int pos,int pre)
{
    siz[pos]=1;
    for(int a=head[pos];a;a=net[a].next)
    {
        if(net[a].to!=pre)
        {
            dfs(net[a].to,pos);
            siz[pos]+=siz[net[a].to];
            son[pos].push_back((poi){net[a].to,hs[net[a].to],hs[net[a].to]});
        }
    }
    calc_hash(pos,siz[pos]);
}
void change(int pos,int pre,ll hs_pre)
{
    if(pre)
    {
        son[pos].push_back((poi){pre,hs_pre,hs_pre});
        calc_hash(pos,n);
    }
    for(int a=son[pos].size()-2,b=0;~a;a--)
    {
        son[pos][a].suf+=son[pos][a+1].suf*bs[1];
    }
    ll stp=0;
    son[pos].push_back((poi){0,0,0}); 
    for(int a=0,b=son[pos].size()-1;a<b;a++)
    {
        if(son[pos][a].n!=pre)
        {
            change(son[pos][a].n,pos,stp+bs[a+1]*son[pos][a+1].suf+n-siz[son[pos][a].n]);
        }
        stp+=bs[a+1]*son[pos][a].w;
    }
}
void Clear()
{
    tot=0;
    memset(head,0,sizeof(head));
    memset(deg,0,sizeof(deg));
    memset(hs,0,sizeof(hs));
    for(int a=1;a<=n;a++)
    {
        son[a].clear();
    }
}
int main()
{
    scanf("%d",&n);
    get_base(1011139,n);
    for(int a=1,b,c;a<n;a++)
    {
        scanf("%d%d",&b,&c);
        add(b,c);
    }
    dfs(1,0);
    change(1,0,0);
    for(int a=1;a<=n;a++)
    {
        mp[hs[a]]=1;
    }
    Clear(),n++;
    for(int a=1,b,c;a<n;a++)
    {
        scanf("%d%d",&b,&c);
        add(b,c);
    }
    dfs(1,0);
    change(1,0,0);
    for(int a=1;a<=n;a++)
    {
        if(deg[a]==1)
        {
            if(mp[son[net[head[a]].to][1].suf*bs[1]+n-1])
            {
                printf("%d",a);
                break;
            }
        }
    }
    return 0;
}
