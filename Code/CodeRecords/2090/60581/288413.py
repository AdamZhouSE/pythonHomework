#include<bits/stdc++.h>
#define Rg register
#define fp(i,a,b) for(Rg int i=(a),I=(b)+1;i<I;++i)
#define fd(i,a,b) for(Rg int i=(a),I=(b)-1;i>I;--i)
#define go(G,u) for(Rg int i=G.head[u],v=G.e[i].to;i;v=G.e[i=G.e[i].nxt].to)
#define P pair<ll,int>
#define ll long long
using namespace std;
const ll inf=1e18+7;
const int M=1e5+3;
#ifndef Judge
#define getchar() (p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++)
#endif
char buf[1<<21],*p1=buf,*p2=buf;
inline int Max(int x,int y){return x>y?x:y;}
inline int Min(int x,int y){return x<y?x:y;}
inline bool cmax(ll& a,ll b){return a<b?a=b,1:0;}
inline bool cmin(ll& a,ll b){return a>b?a=b,1:0;}
inline int read(){ int x=0,f=1; char c=getchar();
    for(;!isdigit(c);c=getchar()) if(c=='-') f=-1;
    for(;isdigit(c);c=getchar()) x=x*10+c-'0'; return x*f;
} int T,n,L,u,v,xb,frm[M],a[M],vis[M];
ll l,r,m,md,le[M],di[M]; P b[M],c[M];
struct Gr{ int pat,head[M];
    struct Edge{ int to,val,nxt; }e[M<<1];
    inline void clear(int n){
        pat=1,memset(head,0,(n+2)<<2);
    }
    inline void add(int u,int v,int w){
        e[++pat]={v,w,head[u]},head[u]=pat;
        e[++pat]={u,w,head[v]},head[v]=pat;
    }
}G;
void dfs(int u,int fa,ll d){
    if(d>md) md=d,v=u;
    go(G,u) if(v^fa&&!vis[i>>1])
        frm[v]=i,dfs(v,u,d+G.e[i].val);
}
int main(){
    while(1){ n=read(),L=read();
        if(!n) return 0; int x,y,z,i,flg;
        G.clear(n),memset(vis,0,n<<2);
        fp(i,2,n) x=read(),y=read(),
            z=read(),G.add(x,y,z);
        md=0,dfs(1,0,0),md=0,u=v,dfs(v,0,0);
        for(i=v,xb=0;i^u;i=G.e[frm[i]^1].to)
            vis[frm[i]>>1]|=1,a[++xb]=i,
            di[xb+1]=di[xb]+G.e[frm[i]].val;
        a[++xb]=i;
        fp(i,1,xb) md=0,dfs(a[i],0,0),le[i]=md,
            c[i]=P(le[i]+di[i],i),b[i]=P(le[i]-di[i],i);
        sort(b+1,b+1+xb),sort(c+1,c+1+xb);
        for(l=le[xb],r=di[xb];l<r;flg?r=m:l=m+1){
            ll A=-inf,B=inf,C=-inf,D=inf,aa=-inf,bb=inf; flg=0,m=(l+r)>>1;
            for(Rg int i=1,j=xb+1;i<=xb;++i){
                for(;j>1&&c[j-1].first+b[i].first>m;) u=c[--j].second,
                    cmax(aa,di[u]+le[u]),cmin(bb,di[u]-le[u]); u=b[i].second;
                cmax(A,L-m+le[u]+di[u]+aa),cmin(B,m-L+di[u]-le[u]+bb);
                cmax(C,le[u]-di[u]+L-m+aa),cmin(D,m-L-di[u]-le[u]+bb);
            }
            if(A>B||C>D){l=m+1;continue;}
            Rg int i,j,k,p,q;
            for(i=j=k=1,p=q=xb;!flg&&i<=xb;++i){
                while(j<i&&di[i]-di[j+1]>=C)++j;
                while(di[i]-di[k]>D)++k;
                while(p&&di[i]+di[p-1]>=A)--p;
                while(q&&di[i]+di[q]>B)--q;
                if(di[i]-di[j]>=C&&di[i]-di[k]<=D&&di[i]+di[p]>=A
                    &&di[i]+di[q]<=B&&Max(k,p)<=Min(j,q)) flg=1;
            }
        } printf("%lld\n",l);
    }
}  