#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long LL;
const LL mod=998244353;
struct node
{
    int x,y,next;
}a[610000];int len,last[310000];
void ins(int x,int y){len++;a[len].x=x;a[len].y=y;a[len].next=last[x];last[x]=len;}
int col[310000];
int bin[25],fa[310000][25];
LL dep[310000];
inline void pre_tree_node(int x)
{
    for(register int i=1;bin[i]<=dep[x];++i)fa[x][i]=fa[fa[x][i-1]][i-1];
    for(register int k=last[x];k;k=a[k].next)
    {
        int y=a[k].y;
        if(y!=fa[x][0])
        {
            dep[y]=dep[x]+1;
            fa[y][0]=x;
            pre_tree_node(y);
        }
    }
}
LL sx[310000][55];
inline LL pow_mod(int a,int b)
{
    register LL ret=1;
    while(b)
    {
        if(b&1)ret=(LL)ret*a%mod;
        a=(LL)a*a%mod;b>>=1;
    }
    return ret;
}
void work(int x)
{
    for(int i=1;i<=50;i++)sx[x][i]=sx[fa[x][0]][i]+pow_mod(dep[x]-1,i);
    for(int k=last[x];k;k=a[k].next)
    {
        int y=a[k].y;
        if(y!=fa[x][0])work(y);
    }
}
int lca(int x,int y)
{
    if(dep[x]<dep[y])swap(x,y);
    for(int i=20;i>=0;i--)if(bin[i]<=dep[x] && dep[fa[x][i]]>=dep[y])x=fa[x][i];
    if(x==y)return x;
    for(int i=20;i>=0;i--)if(bin[i]<=dep[x] && fa[x][i]!=fa[y][i])x=fa[x][i],y=fa[y][i];
    return fa[x][0]; 
}
LL findsum(int x,int y,int op)
{
    int LA=lca(x,y);
    return (LL)(sx[x][op]+sx[y][op]-sx[LA][op]-sx[fa[LA][0]][op])%mod;
}
int n,m;
LL ans[310000];
int main()
{
    bin[0]=1;for(int i=1;i<=20;i++)bin[i]=bin[i-1]*2;
    scanf("%d",&n);
    for(int i=1;i<n;i++)
    {
        int x,y;scanf("%d%d",&x,&y);
        ins(x,y);ins(y,x);
    }
    fa[1][0]=0;dep[1]=1;
    pre_tree_node(1);
    work(1);
    scanf("%d",&m);
    for(int i=1;i<=m;i++)
    {
        int x,y,op;scanf("%d%d%d",&x,&y,&op);
        printf("%lld\n",findsum(x,y,op));
    }
    return 0;
}