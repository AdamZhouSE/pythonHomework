#include<iostream>
#include<queue>
#include<cstring>
using namespace std;
const int N=4e4+10;
struct edge{int next,to;}a[N];
int n,m,head[N],cnt,del[N],col[N],flag,tt,sn,sm,p1,p2,du[N];
queue<int> Q;
void link(int x,int y) {a[++cnt]=(edge){head[x],y};head[x]=cnt;}
void dfs(int x,int c)
{
    col[x]=c;sn++;if(flag) return;
    int son=0;
    for(int i=head[x];i;i=a[i].next)
    {
        int R=a[i].to;if(del[R]) continue;
        sm++;son++;
        if(col[R]&&col[R]!=3-c) {flag=1;return;}
        if(!col[R]) dfs(R,3-c);
    }
    if(son==3) p1?p2=x:p1=x;
}
void calc(int x,int fr,int s)
{
    if(x==p2) {tt+=(s==2);return;}
    for(int i=head[x];i;i=a[i].next)
        if(!del[a[i].to]&&a[i].to!=fr)
            calc(a[i].to,x,s+1);
}
void Work()
{NO
    memset(du,0,sizeof(du));
    memset(head,0,sizeof(head));
    memset(col,0,sizeof(col));
    memset(del,0,sizeof(del));
    flag=0;cnt=0;
    cin>>n>>m;
    for(int i=1,x,y;i<=m;i++)
        scanf("%d%d",&x,&y),du[x]++,du[y]++,link(x,y),link(y,x);
    for(int i=1;i<=n;i++) if(du[i]==1) Q.push(i);
    while(!Q.empty())
    {
        int x=Q.front();Q.pop();del[x]=1;
        for(int i=head[x];i;i=a[i].next)
            if(--du[a[i].to]==1) Q.push(a[i].to);
    }
    for(int i=1;i<=n;i++)
        if(!col[i]&&!del[i])
        {
            sn=sm=p1=p2=0;dfs(i,1);sm/=2;
            if(sm>=sn+2||flag) return (void)puts("NO");
            if(sm==sn+1) {calc(p1,0,tt=0);if(tt<2) return (void)puts("NO");}
        }
    puts("YES");
}
int main() {int T;cin>>T;while(T--) Work();}