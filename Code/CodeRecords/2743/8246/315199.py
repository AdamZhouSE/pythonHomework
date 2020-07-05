#include <cstdio>

#define N 300010
#define lc(x) ch[x][0]
#define rc(x) ch[x][1]
#define re register
inline void swap(re int&a,re int&b){re int tmp(a);a=b,b=tmp;}

int ch[N][2],fa[N],rev[N],val[N],addv[N];
inline void add(re int x,re int y){val[x]+=y,addv[x]+=y;}
inline void down(re int x)
{
    if(rev[x])
        rev[lc(x)]^=1,rev[rc(x)]^=1,swap(lc(x),rc(x)),rev[x]=0;
    if(addv[x])
        add(lc(x),addv[x]),add(rc(x),addv[x]),addv[x]=0;
}
inline int nrt(re int x){return x==lc(fa[x])||x==rc(fa[x]);}
void psa(int x){if(nrt(x))psa(fa[x]);down(x);}
inline void rotate(re int x)
{
    re int y(fa[x]),z(fa[y]),k(x==rc(y));
    ch[y][k]=ch[x][!k],ch[x][!k]=y;if(nrt(y))ch[z][y==rc(z)]=x;
    if(ch[y][k])fa[ch[y][k]]=y;fa[y]=x,fa[x]=z;
}
inline void splay(re int x)
{
    re int y,z;
    for(psa(x);nrt(x);rotate(x))
    {y=fa[x],z=fa[y];if(nrt(y))rotate(x==rc(y)^y==rc(z)?x:y);}
}
inline void access(re int x){for(re int y(0);x;x=fa[y=x])splay(x),rc(x)=y;}
inline void mrt(re int x){access(x),splay(x),rev[x]^=1;}
inline void link(re int x,re int y){mrt(x),fa[x]=y;}

int n,a[N],x,y;

int main()
{
    scanf("%d",&n);
    for(re int i(1);i<=n;++i)
        scanf("%d",a+i);
    for(re int i(1);i<n;++i)
        scanf("%d%d",&x,&y),link(x,y);
    for(re int i(1);i<n;++i)
        --val[a[i+1]],mrt(a[i]),access(a[i+1]),splay(a[i+1]),add(a[i+1],1);
    for(re int i(1);i<=n;++i)
        mrt(i),printf("%d\n",val[i]);
    return 0;
}