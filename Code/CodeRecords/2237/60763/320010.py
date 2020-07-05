#include <cstdio>
#define Maxn 100010
#define INF 0x3f3f3f3f
using namespace std;
int f[Maxn],ch[Maxn][2],siz[Maxn],mark[Maxn],key[Maxn],root,sz;
int data[Maxn];
int R() {int x=0,F=1;char C=getchar();while(C<'0'||C>'9'){if(C=='-')F=-F;C=getchar();}while(C>='0'&&C<='9')x=x*10-'0'+C,C=getchar();return x*F;}
inline int get(int x){return ch[f[x]][1]==x;}
inline void update(int x){siz[x]=siz[ch[x][1]]+siz[ch[x][0]]+1;}
inline void swap(int &x,int &y){int t=x;x=y;y=t;}
inline int pushdown(int x)
{
    if (x && mark[x])
    {
        mark[ch[x][0]]^=1;
        mark[ch[x][1]]^=1;
        swap(ch[x][0],ch[x][1]);
        mark[x]=0;
    }
}
inline int rot(int x)
{
    int k=get(x),fa=f[x],fafa=f[fa];
    pushdown(fa);pushdown(x);
    ch[fa][k]=ch[x][!k];f[ch[x][!k]]=fa;
    ch[x][!k]=fa;f[fa]=x;
    f[x]=fafa;
    if (fafa) ch[fafa][ch[fafa][1]==fa]=x;
    update(fa);update(x);
}
inline int splay(int x,int tar)
{
    for (int fa;(fa=f[x])!=tar;rot(x))
        if (f[fa]!=tar)
            rot(get(fa)==get(x)?fa:x);
    if (!tar) root=x;
}
inline int build(int fa,int l,int r)
{
    if (l>r) return 0;
    int mid=(l+r)>>1;
    int now=++sz;
    key[now]=data[mid],f[now]=fa,mark[now]=0;
    ch[now][0]=build(now,l,mid-1);
    ch[now][1]=build(now,mid+1,r);
    update(now);
    return now;
}
inline int findx(int k)
{
    int now=root;
    while(1)
    {
        pushdown(now);
        if (k<=siz[ch[now][0]])
            now=ch[now][0];
        else
        {
            k-=siz[ch[now][0]]+1;
            if (!k) return now;
            now=ch[now][1];
        }
    }
}
inline void print(int now)
{
    pushdown(now);
    if (ch[now][0]) print(ch[now][0]);
    if (key[now]!=-INF && key[now]!=INF)
      printf("%d ",key[now]);
    if (ch[now][1]) print(ch[now][1]);
}
main()
{
    int n,m,x,y;
    scanf("%d %d",&n,&m);
    for (int i=1;i<=n;i++)
        data[i+1]=i;
    data[1]=-INF,data[n+2]=INF;
    root=build(0,1,n+2);
    for (int i=1;i<=m;i++)
    {
        x=R();
        y=R();
        int x1=findx(x),y1=findx(y+2);
        splay(x1,0);
        splay(y1,x1);
        mark[ch[ch[root][1]][0]]^=1;
    }
    print(root);
}