#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define dep(i,a,b) for(int i=a;i>=b;i--)
#define ll long long
#define mem(x,num) memset(x,num,sizeof x)
#define reg(x) for(int i=last[x];i;i=e[i].next)
using namespace std;
inline ll read()
{
    ll f=1,x=0;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
const int maxn=1e3+6;
struct edge{int to,next;}e[maxn<<1];
int n,m,T,low[maxn],dfn[maxn],top,que[maxn<<2],last[maxn],tim,cnt,cas,deg,tot,num,vis[maxn],ans1,root;
bool cut[maxn],inque[maxn];ll ans2;
void insert(int u,int v){
    e[++cnt]=(edge){v,last[u]};last[u]=cnt;
    e[++cnt]=(edge){u,last[v]};last[v]=cnt;
}
void tarjan(int x){
    dfn[x]=low[x]=++tim;que[++top]=x;inque[x]=1;
    reg(x){
        if(!dfn[e[i].to]){tarjan(e[i].to);low[x]=min(low[x],low[e[i].to]);}
        else if(inque[e[i].to]){low[x]=min(low[x],dfn[e[i].to]);continue;}
        if(dfn[x]<=low[e[i].to]){if(x==root)deg++;else cut[x]=1;}
    }
}
void dfs(int x){
    vis[x]=T;if(cut[x])return;tot++;
    reg(x){
        if(cut[e[i].to]&&vis[e[i].to]!=T)num++,vis[e[i].to]=T;
        if(!vis[e[i].to])dfs(e[i].to);
    }
}
int main()
{
    while(1){
        m=read();if(!m)break;
        mem(e,0);mem(low,0);mem(dfn,0);mem(cut,0);mem(vis,0);mem(inque,0);mem(que,0);mem(last,0);
        cnt=n=tim=T=ans1=top=0,cas++,ans2=1;
        rep(i,1,m){
            int x=read(),y=read();
            insert(x,y);n=max(n,max(x,y));
        }
        rep(i,1,n){
            if(!dfn[i]){tarjan(root=i);if(deg>=2)cut[root]=1;}
            deg=0;
        }
        rep(i,1,n)
            if(!vis[i]&&!cut[i]){
                ++T,tot=num=0,dfs(i);
                if(!num)ans1+=2,ans2*=tot*(tot-1)/2;
                if(num==1)ans1++,ans2*=tot;
            }
        printf("Case %d: %d %lld\n",cas,ans1,ans2);
    }
    return 0;
}
————————————————
版权声明：本文为CSDN博主「yjjr」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qwerty1125/article/details/79485691