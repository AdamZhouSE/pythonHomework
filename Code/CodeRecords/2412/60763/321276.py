#include<bits/stdc++.h>

#define REP(i,a,b) for(int i=a,i##_end_=b;i<=i##_end_;++i)
#define DREP(i,a,b) for(int i=a,i##_end_=b;i>=i##_end_;--i)
#define pii pair<int,int>
#define fi first
#define se second
#define mk make_pair
typedef long long ll;

using namespace std;

template<typename T>void read(T &_){
    T __=0,mul=1; char ch=getchar();
    while(!isdigit(ch)){
        if(ch=='-')mul=-1;
        ch=getchar();
    }
    while(isdigit(ch))__=(__<<1)+(__<<3)+(ch^'0'),ch=getchar();
    _=__*mul;
}

void File(){
    freopen("gen.in","r",stdin);
    freopen("gen.out","w",stdout);
}

const int maxn=2e5+10;
int n,m,a[maxn],to[maxn],ans,cnt,tot,num[maxn];
pii b[maxn];
bool yes[maxn],vis[maxn];

int fa[maxn];
int find(int x){return fa[x]==x ? x : fa[x]=find(fa[x]);}

void init(){
    read(n); read(m);
    REP(i,1,n)read(a[i]),b[i]=mk(a[i],i);
    sort(b+1,b+n+1);
    REP(i,1,n)if(a[i]==b[i].fi)yes[i]=1;
    REP(i,1,n)fa[i]=i;
    int p=1;
    REP(i,1,n){
        if(yes[b[i].se])continue;
        while(yes[p])++p;
        to[b[i].se]=p++;
        fa[find(b[i].se)]=find(to[b[i].se]);
    }
    REP(i,1,n){
        int l=i,r=i,las=0;
        while(b[r+1].fi==b[l].fi)++r;
        REP(j,l,r){
            if(yes[b[j].se])continue;
            if(!las){las=j;continue;}
            if(find(b[las].se)==find(b[j].se))continue;
            fa[find(b[las].se)]=find(b[j].se);
            swap(to[b[las].se],to[b[j].se]);
            las=j;
        }
        i=r;
    }
}

int Mincost(){return tot<=2 ? cnt : tot+cnt;}

int solve(int x){
    int qu[maxn],q=0,p=to[x];
    qu[++q]=x;
    while(p!=x)qu[++q]=p,p=to[p];
    printf("%d\n",q);
    REP(i,1,q)printf("%d ",qu[i]);
    putchar('\n');
    return q;
}

void work(){
    REP(i,1,n){
        if(yes[i])continue;
        ++cnt;
        if(!vis[find(i)]){
            num[++tot]=find(i);
            vis[find(i)]=1;
        }
    }
    if(cnt>m){puts("-1");return;}
    if((tot>2 ? cnt+tot : cnt)<=m)ans=2;
    else ans=2+cnt+tot-m;
    ans=min(ans,tot);
    printf("%d\n",ans);
    while((tot>1 ? cnt+tot : cnt)>m){
        int cost=solve(num[tot]);
        m-=cost; cnt-=cost; --tot;
    }
    if(tot==1)solve(num[tot]);
    else if(tot){
        int qu[maxn],q1[maxn],q=0,qq=0;
        while(tot){
            int p=to[num[tot]]; qu[++q]=num[tot]; q1[++qq]=num[tot];
            while(p!=num[tot])qu[++q]=p,p=to[p];
            --tot;
        }
        printf("%d\n",q);
        REP(i,1,q)printf("%d ",qu[i]);
        putchar('\n');
        printf("%d\n",qq);
        DREP(i,qq,1)printf("%d ",q1[i]);
        putchar('\n');
    }
} 
int main(){
    File();
    init();
    work();
    return 0;
}