#include<bits/stdc++.h>
using namespace std;
int read() {
    int q=0,w=1;char ch=' ';
    while(ch!='-'&&(ch<'0'||ch>'9')) ch=getchar();
    if(ch=='-') w=-1,ch=getchar();
    while(ch>='0'&&ch<='9') q=q*10+ch-'0',ch=getchar();
    return q*w;
}
typedef long long LL;
typedef double db;
const int N=200005,M=1200005;const db eps=1e-10;
#define RI register int
int n,m,Q,tot=1,cnt,rt;LL ans1,ans2;
struct point{int x,y;}p[N];
point operator - (point a,point b) {return (point){a.x-b.x,a.y-b.y};}
LL operator * (point a,point b) {return 1LL*a.x*b.y-1LL*a.y*b.x;}
struct edge{int id,u,v;db jd;}e[M];
bool operator < (edge a,edge b) {return fabs(a.jd-b.jd)<eps?a.v<b.v:a.jd<b.jd;}
int nxt[M],pos[M],f[M],vis[M],istr[M],ask[M];LL s[M],ss[M];
vector<edge> h[N],tr[M];

void link(int x,int y) {
    ++tot,e[tot]=(edge){tot,x,y,atan2(p[y].y-p[x].y,p[y].x-p[x].x)};
    h[x].push_back(e[tot]);
}
void build() {
    for(RI i=1;i<=n;++i) sort(h[i].begin(),h[i].end());
    for(RI i=2;i<=tot;++i) {
        int v=e[i].v;
        vector<edge>::iterator kl=lower_bound(h[v].begin(),h[v].end(),e[i^1]);
        if(kl==h[v].begin()) kl=h[v].end();//其前一条就是最后一条
        --kl,nxt[i]=(*kl).id;
    }
    for(RI i=2;i<=tot;++i) {
        if(pos[i]) continue;
        pos[i]=pos[nxt[i]]=++cnt;
        for(RI j=nxt[i];e[j].v!=e[i].u;j=nxt[j],pos[j]=cnt)
            s[cnt]+=(p[e[j].u]-p[e[i].u])*(p[e[j].v]-p[e[i].u]);//计算面积
        if(s[cnt]<=0) rt=cnt;//无穷域
    }
    for(RI i=2;i<=tot;++i) tr[pos[i]].push_back((edge){i,pos[i],pos[i^1]});
}
void dfs(int x,int las) {//生成树
    f[x]=las,ss[x]=1LL*s[x]*s[x],s[x]<<=1,vis[x]=1;
    //叉积算面积后应该除以2，但是为了避免小数，所以分子分母同时乘4
    for(RI i=0,sz=tr[x].size();i<sz;++i) {
        int v=tr[x][i].v;
        if(vis[v]) continue;
        istr[tr[x][i].id]=istr[tr[x][i].id^1]=1,dfs(v,x);
        s[x]+=s[v],ss[x]+=ss[v];
    }
}

LL gcd(LL a,LL b) {return b?gcd(b,a%b):a;}
void work() {
    while(Q--) {
        int js=(read()+ans1)%n+1;
        for(RI i=1;i<=js;++i) ask[i]=(read()+ans1)%n+1;
        ask[js+1]=ask[1],ans1=ans2=0;
        for(RI i=1;i<=js;++i) {
            int x=ask[i],y=ask[i+1];
            edge ke=(edge){0,x,y,atan2(p[y].y-p[x].y,p[y].x-p[x].x)};
            vector<edge>::iterator kl=lower_bound(h[x].begin(),h[x].end(),ke);//找边
            int j=(*kl).id;
            if(!istr[j]) continue;//该边所在区域，是儿子就加是父亲就减
            if(f[pos[j]]==pos[j^1]) ans1+=ss[pos[j]],ans2+=s[pos[j]];
            else ans1-=ss[pos[j^1]],ans2-=s[pos[j^1]];
        }
        LL tmp=gcd(ans1,ans2);
        ans1/=tmp,ans2/=tmp;
        printf("%lld %lld\n",ans1,ans2);
    }
}

int main()
{
    int x,y;
    n=read(),m=read(),Q=read();
    for(RI i=1;i<=n;++i) p[i]=(point){read(),read()};
    for(RI i=1;i<=m;++i) x=read(),y=read(),link(x,y),link(y,x);
    build(),dfs(rt,0),work();
    return 0;
}