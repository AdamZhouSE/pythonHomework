#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 50
int lowbit(int x){return x&-x;} 
struct treearr{
    int c[maxn],siz;
    void init(int p){int i;for(i=1;i<=p;++i)c[i]=0;siz=p;}
    void add(int x,int d){while(x<=siz){c[x]+=d;x+=lowbit(x);}}
    int sum(int x){int res=0;while(x){res+=c[x];x-=lowbit(x);}return res;}
    int query(int l,int r){return sum(r)-sum(l-1);}
};
treearr up,down;
int n,a[maxn],pos,l[maxn],r[maxn],ans;
void dfs(int st,int sum){
    if(st>pos){
        ans=min(ans,sum);return;
    }
    if(sum>ans)return;
    int i;
    int a1=min(up.query(l[st],r[st]),down.query(l[st],n)+up.query(r[st],n));
    up.add(r[st],1);dfs(st+1,sum+a1);up.add(r[st],-1);
    int a2=min(down.query(l[st],r[st]),up.query(l[st],n)+down.query(r[st],n));
    down.add(r[st],1);dfs(st+1,sum+a2);down.add(r[st],-1);
}
int main(){
    int T;scanf("%d",&T);
    while(T--){
        int i,j;scanf("%d",&n);ans=1<<30;
        for(i=1;i<=n;++i)scanf("%d",&a[i]);
        pos=0;
        for(i=1;i<=n;++i)
            for(j=i+2;j<=n;++j)if(a[i]==a[j])
            {
                l[++pos]=i,r[pos]=j;break;
            }
        up.init(n);down.init(n);
        dfs(1,0);
        printf("%d\n",ans);
    }
}