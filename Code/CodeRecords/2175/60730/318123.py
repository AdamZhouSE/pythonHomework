#include<bits/stdc++.h>
using namespace std;

#define int long long 

void read(int &x) {
    x=0;int f=1;char ch=getchar();
    for(;!isdigit(ch);ch=getchar()) if(ch=='-') f=-f;
    for(;isdigit(ch);ch=getchar()) x=x*10+ch-'0';x*=f;
}

void print(int x) {
    if(x<0) putchar('-'),x=-x;
    if(!x) return ;print(x/10),putchar(x%10+48);
}
void write(int x) {if(!x) putchar('0');else print(x);putchar('\n');}

#define lf double
#define ll long long 

#define pii pair<int,int >
#define vec vector<int >

#define pb push_back
#define mp make_pair
#define fr first
#define sc second

#define FOR(i,l,r) for(int i=l,i##_r=r;i<=i##_r;i++)

const int maxn = 1e6+10;
const int inf = 1e9;
const lf eps = 1e-8;
const int mod = 1e9+7;

int head[maxn],tot,sz[maxn],n,f[maxn],rev[maxn];
struct edge{int to,nxt;}e[maxn<<1];

struct P {
    int x,y,id;

    P operator - (const P &r) const {return (P){x-r.x,y-r.y};}
    ll operator * (const P &r) const {return 1ll*x*r.y-y*r.x;}
};

void ins(int u,int v) {e[++tot]=(edge){v,head[u]},head[u]=tot;}

void dfs(int x,int fa) {
    sz[x]=1;f[x]=fa;
    for(int i=head[x];i;i=e[i].nxt)
        if(e[i].to!=fa) dfs(e[i].to,x),sz[x]+=sz[e[i].to];
}

int cmp1(P x,P y) {return x.x<y.x||(x.x==y.x&&x.y<y.y);}

P pp;

int cmp(P x,P y) {return (x-pp)*(y-pp)>0;}

void solve(int x,vector<P > t) {
    sort(t.begin(),t.end(),cmp1);
    auto xx=t.begin();xx++;pp=t[0];
    sort(xx,t.end(),cmp);
    rev[x]=t[0].id;
    int p=1;
    for(int i=head[x];i;i=e[i].nxt) {
        int v=e[i].to;if(v==f[x]) continue;
        vector<P > tt;tt.clear();
        for(int w=p;w<p+sz[v];w++) tt.pb(t[w]);
        solve(v,tt);p+=sz[v];
    }
}

void dfs2(int x,int fa) {
    for(int i=head[x];i;i=e[i].nxt)
        if(e[i].to!=fa) printf("%lld %lld\n",rev[x]-1,rev[e[i].to]-1),dfs2(e[i].to,x);
}

signed main() {
    vector<P > a;read(n);
    for(int i=1,x,y;i<n;i++) read(x),read(y),x++,y++,ins(x,y),ins(y,x);
    dfs(1,0);
    for(int i=1,x,y;i<=n;i++) read(x),read(y),a.pb((P){x,y,i});
    solve(1,a);
    dfs2(1,0);
    return 0;
}