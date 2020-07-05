#include<bits/stdc++.h>
using namespace std;
#define rint register int 
#define ll long long

inline int read(){
    int x=0,f=0;char ch=getchar();
    while(!isdigit(ch))    f=(ch==45),ch=getchar();
    while( isdigit(ch))    x=(x<<1)+(x<<3)+(ch^48),ch=getchar();
    return f?(~x+1):x;
}

#define man 200050

struct edge{int next,to,dis;}e[man<<1];
int head[man<<1],num=0;

inline void add(int from,int to,int dis){
    e[++num]=(edge){head[from],to,dis};
    head[from]=num;
}
int n,m;
int vis[man];
ll dis0[man],disa[man],disb[man];

inline int spfa(int s,ll dis[]){
    for(rint i=1;i<=n;i++) dis[i]=2e11+9,vis[i]=0;
    queue<int>q;
    q.push(s);dis[s]=0;vis[s]=1;
    do{
        int u=q.front();q.pop();vis[u]=0;
        for(rint i=head[u];i;i=e[i].next){
            int to=e[i].to;
            if(dis[to]>dis[u]+e[i].dis){
                dis[to]=dis[u]+e[i].dis;
                if(!vis[to]){
                    vis[to]=1;
                    q.push(to);
                }
            }
        }
    }while(!q.empty());
    ll maxn=0;int pos=s;
    for(rint i=1;i<=n;i++){
        if(maxn<dis[i]) maxn=dis[i],pos=i;
    }
    return pos;
}

int main(){
    n=read();m=read();
    for(rint i=1,x,y,z;i<=m;i++){
        x=read();y=read();z=read();
        add(x,y,z);add(y,x,z);
    }
    rint a=spfa(1,dis0);
    rint b=spfa(a,disa);
    spfa(b,disb);
    ll ans=disa[b],maxn=0;
    for(rint i=1;i<=n;i++)
        maxn=max(maxn,min(disa[i],disb[i]));
    printf("%lld\n",ans+maxn);
    return 0;
}