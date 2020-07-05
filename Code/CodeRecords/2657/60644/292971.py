#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<cstring>
#include<cstdio>
using namespace std;
 
int read()
{
    int f=1,x=0;
    char ss=getchar();
    while(ss<'0'||ss>'9'){if(ss=='-')f=-1;ss=getchar();}
    while(ss>='0'&&ss<='9'){x=x*10+ss-'0';ss=getchar();}
    return f*x;
}

int n,m;
struct node{int v,nxt;}E[300010];
int head[200010],tot;
int dep[200010],fa[200010],son[200010],size[200010];
int top[200010],num[500010],pos[500010],cnt;
int sum[500010];

void add(int u,int v)
{
    E[++tot].nxt=head[u];
    E[tot].v=v;
    head[u]=tot;
} 

void dfs1(int u,int pa)
{
    size[u]=1;
    for(int i=head[u];i;i=E[i].nxt)
    {
        int v=E[i].v;
        if(v==pa) continue;
        dep[v]=dep[u]+1;  fa[v]=u;
        dfs1(v,u);
        size[u]+=size[v];
        if(size[v]>size[son[u]]) son[u]=v;
    }
}

void dfs2(int u,int tp)
{
    num[u]=++cnt; pos[cnt]=u; top[u]=tp;
    if(son[u]) dfs2(son[u],tp);
    for(int i=head[u];i;i=E[i].nxt)
    {
        int v=E[i].v;
        if(v==fa[u]||v==son[u]) continue;
        dfs2(v,v);
    }
}

void update(int u,int s,int t,int p)
{
    if(s==t){sum[p]=1; return;}
    int mid=s+t>>1;
    if(u<=mid) update(u,s,mid,p<<1);
    else update(u,mid+1,t,p<<1|1);
    sum[p]=sum[p<<1]+sum[p<<1|1];
}

int get(int ll,int rr,int s,int t,int p)
{
    if(ll<=s&&t<=rr) return sum[p];
    int mid=s+t>>1;
    int ans=0;
    if(ll<=mid) ans+=get(ll,rr,s,mid,p<<1);
    if(rr>mid) ans+=get(ll,rr,mid+1,t,p<<1|1);
    return ans;
}

int check(int ll,int rr)
{
    if(ll==rr) return ll;
    int mid=ll+rr>>1;
    int tp=get(mid+1,rr,1,n,1);
    if(tp>=1) return check(mid+1,rr);
    else return check(ll,mid);
}

int query(int u)
{
    while(top[u]!=1)
    {
        int tp=get(num[top[u]],num[u],1,n,1);
        if(tp>=1) return check(num[top[u]],num[u]);
        u=fa[top[u]];
    }
    return check(1,num[u]);
}

int main()
{
    n=read();m=read();
    for(int i=1;i<n;++i)
    {
        int u=read(),v=read();
        add(u,v);add(v,u);
    }
    
    dep[1]=1;
    dfs1(1,0); dfs2(1,1);
    sum[num[1]]=1;
    
    while(m--)
    {
        char ss; scanf("%s",&ss);
        int u=read();
        if(ss=='C') update(num[u],1,n,1);
        else if(ss=='Q') printf("%d\n",pos[query(u)]);
    }
    return 0;
}
