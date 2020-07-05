#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#define ll long long
using namespace std;
inline int read(){
    int x=0,o=1;char ch=getchar();
    while(ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();
    if(ch=='-')o=-1,ch=getchar();
    while(ch>='0'&&ch<='9')x=x*10+ch-'0',ch=getchar();
    return x*o;
}
const int N=3005;
const int M=8005;
int n,m,p,ans;
int a[M],b[M],deg[N],val[N];
int tot,head[N],nxt[M],to[M];
int top,sum,timeclock;
int dfn[N],low[N],st[N],color[N],size[N];
inline void add(int a,int b){
    nxt[++tot]=head[a];head[a]=tot;to[tot]=b;
}
inline void tarjan(int u){
    dfn[u]=low[u]=++timeclock;
    st[++top]=u;
    for(int i=head[u];i;i=nxt[i]){
        int v=to[i];
        if(!dfn[v]){
            tarjan(v);
            low[u]=min(low[u],low[v]);
        }
        else if(!color[v]){
            low[u]=min(low[u],dfn[v]);
        }
    }
    if(low[u]==dfn[u]){
        color[u]=++sum;
        if(val[u])size[sum]=min(size[sum],val[u]);
//处理好每个强连通分量里最小的权值,一定要有值才能更新
        while(st[top]!=u){
            color[st[top]]=sum;
            if(val[st[top]])size[sum]=min(size[sum],val[st[top]]);
            --top;
        }
        --top;
    }
}
int main(){
    n=read();p=read();
    for(int i=1;i<=p;++i){
        int x=read(),y=read();
        val[x]=y;
    }
    m=read();
    for(int i=1;i<=m;++i){
        a[i]=read(),b[i]=read();
        add(a[i],b[i]);
    }
    for(int i=1;i<=n;++i)size[i]=1e9;//初始化极大值
    for(int i=1;i<=n;++i)if(!dfn[i])tarjan(i);
    tot=0;memset(head,0,sizeof(head));
    for(int i=1;i<=m;++i){//重新建图
        if(color[a[i]]!=color[b[i]]){
            add(color[a[i]],color[b[i]]);
            ++deg[color[b[i]]];
        }
    }
    for(int i=1;i<=n;++i)//先特判
        if(size[color[i]]==1e9&&!deg[color[i]]){
            printf("NO\n%d\n",i);return 0;
        }
    for(int i=1;i<=sum;++i)
        if(!deg[i])ans+=size[i];
    printf("YES\n%d\n",ans);
    return 0;
}
