#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
using namespace std;

char BUF[2000001],*buf,*end;
#define getch() (buf==end?fread(BUF,1,2000000,stdin),buf=BUF,end=buf+2000000,*(buf++):*(buf++))
inline void Read(int &x){
    static char c;
    int f=1;
    for(c=getchar();c<'0'||c>'9';c=getchar()) if(c=='-') f=-1;
    for(x=0;c>='0'&&c<='9';c=getchar()) x=x*10+c-'0';
    x=x*f;
}

const int N=200010;
typedef long long ll;
struct point{
    int x,y;
    friend ll operator *(const point &a,const point &b){
        return (ll)a.x*b.y-(ll)b.x*a.y;
    }
    friend point operator -(const point &a,const point &b){
        point tmp;
        tmp.x=a.x-b.x; tmp.y=a.y-b.y;
        return tmp;
    }
}p[N];
struct edge{
    int u,v,id;
    double ang;
    edge(){}
    edge(int a,int b,int k){
        u=a; v=b; id=k;
        ang=atan2((double)p[b].y-p[a].y,(double)p[b].x-p[a].x);
    }
    friend bool operator <(const edge &a,const edge &b){
        return a.ang<b.ang;
    }
}e[6*N];
vector<edge> E[N],TE[N*2];
int Nex[N*6],v[N*6],cnt=1,num,rt;
int vi[N*2],fa[N*2],flag[N*6];
int n,m,k,x,y,rec,q[N];
ll ans1,ans2,P,S[N*2],S1[N*2];

int Find(int x,const edge &a){
    int mid,l=0,r=E[x].size();
    while(r-l>1){
        mid=(l+r)>>1;
        if(a<E[x][mid]) r=mid;
        else l=mid;
    }
    return l;
}
ll gcd(ll a,ll b){
    if(b==0) return a;
    return gcd(b,a%b);
}
void solve(){
    int now,tmp,st; ll s;
    for(int i=2;i<=cnt;i++)
    if(!v[i]){
        s=0; now=i; v[i]=++num; st=e[i].u;
        while(1){
            tmp=Nex[now]; v[tmp]=num;
            if(e[tmp].v==st) break;
            s+=(p[e[tmp].u]-p[st])*(p[e[tmp].v]-p[st]);
            now=tmp;
        }
        S[num]=s;
        if(s<=0) rt=num;
    }
    for(int i=2;i<=cnt;i++) 
    TE[v[i]].push_back(edge(v[i],v[i^1],i));
}
void dfs(int x){
    vi[x]=1; S1[x]=S[x]*S[x]; S[x]*=2;
    for(int i=0;i<(int)TE[x].size();i++)
    if(!vi[TE[x][i].v]){
        fa[TE[x][i].v]=x;
        flag[TE[x][i].id]=1;
        flag[TE[x][i].id^1]=1;
        dfs(TE[x][i].v);
        S[x]+=S[TE[x][i].v];
        S1[x]+=S1[TE[x][i].v];
    }
}
int main(){
    Read(n); Read(m); Read(k);
    for(int i=1;i<=n;i++) Read(p[i].x),Read(p[i].y);
    for(int i=1;i<=m;i++) {
        Read(x); Read(y);
        ++cnt; e[cnt]=edge(x,y,cnt);
        E[x].push_back(e[cnt]);
        ++cnt; e[cnt]=edge(y,x,cnt);
        E[y].push_back(e[cnt]);
    }
    for(int i=1;i<=n;i++) sort(E[i].begin(),E[i].end());
    for(int i=2;i<=cnt;i++){
        Nex[i]=Find(e[i].v,e[i^1])-1;
        if(Nex[i]<0) Nex[i]=E[e[i].v].size()-1;
        Nex[i]=E[e[i].v][Nex[i]].id;
    }
    solve(); dfs(rt);
    for(int i=1;i<=k;i++){
        Read(q[0]); q[0]=(q[0]+P)%n+1;
        for(int j=1;j<=q[0];j++) Read(q[j]),q[j]=(q[j]+P)%n+1;
        ans1=ans2=0; q[++q[0]]=q[1];
        for(int j=1;j<q[0];j++){
            x=q[j]; y=q[j+1];
            int tmp=Find(x,edge(x,y,0));
            tmp=E[x][tmp].id;
            if(!flag[tmp]) continue;
            if(v[tmp]==fa[v[tmp^1]]) ans1+=S[v[tmp^1]],ans2+=S1[v[tmp^1]];
            else ans1-=S[v[tmp]],ans2-=S1[v[tmp]];
        }
        if(ans1<0) ans1=-ans1,ans2=-ans2;
        ll d=gcd(ans1,ans2); ans1/=d; ans2/=d;
        printf("%lld %lld\n",P=ans2,ans1);
    }
    return 0;
}
