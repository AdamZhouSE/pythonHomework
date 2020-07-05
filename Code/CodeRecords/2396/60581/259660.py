#include <algorithm>
#include <cstdio>
using std::sort;
inline char gc()
{
    static char now[1<<16],*s,*t;
    if(s==t) {t=(s=now)+fread(now,1,1<<16,stdin); if(s==t) return EOF;}
    return *s++;
}
inline int read()
{
    int x=0; char ch=gc();
    while(ch<'0'||'9'<ch) ch=gc();
    while('0'<=ch&&ch<='9') x=x*10+ch-'0',ch=gc();
    return x;
}
inline void swap(int &x,int &y) {int t; t=x,x=y,y=t;}
const int N=2e5+10;
int n,a[N];
int rt,fa[N],ch[N][2],siz[N]; bool rev[N];
int wh(int p) {return p==ch[fa[p]][1];}
void update(int p) {siz[p]=siz[ch[p][0]]+1+siz[ch[p][1]];}
void rever(int p) {rev[p]^=1; swap(ch[p][0],ch[p][1]);}
void pushdw(int p) {if(rev[p]) rever(ch[p][0]),rever(ch[p][1]),rev[p]=false;}
void rotate(int p)
{
    int q=fa[p],r=fa[q],w=wh(p);
    fa[p]=r; if(r) ch[r][wh(q)]=p;
    fa[ch[q][w]=ch[p][w^1]]=q;
    fa[ch[p][w^1]=q]=p;
    update(q),update(p);
}
void pushdwRt(int p) {if(fa[p]) pushdwRt(fa[p]); pushdw(p);}
void splay(int p,int &k)
{
    pushdwRt(p); int t=fa[k];
    for(int q=fa[p];q!=t;rotate(p),q=fa[p]) if(fa[q]!=t) rotate(wh(p)^wh(q)?p:q);
    update(k=p);
}
void bldTr(int &p,int L0,int R0)
{
    if(L0>R0) return;
    int mid=L0+R0>>1; p=a[mid];
    bldTr(ch[p][0],L0,mid-1),bldTr(ch[p][1],mid+1,R0);
    fa[ch[p][0]]=fa[ch[p][1]]=p; update(p);
}
int rnk(int x)
{
    int p=rt;
    while(true)
    {
        pushdw(p);
        if(x<=siz[ch[p][0]]) p=ch[p][0];
        else if(x==siz[ch[p][0]]+1) return p;
        else x-=siz[ch[p][0]]+1,p=ch[p][1];
    }
}
void split(int x,int y)
{
    int p=rnk(x-1),q=rnk(y+1);
    splay(p,rt),splay(q,ch[rt][1]);
}
struct rec{int x,id;} tmp[N];
bool cmpX(rec a,rec b) {return a.x==b.x?a.id<b.id:a.x<b.x;}
void discrete()
{
    for(int i=1;i<=n;i++) tmp[i].x=a[i],tmp[i].id=i;
    sort(tmp+1,tmp+n+1,cmpX);
    for(int i=1;i<=n;i++) a[tmp[i].id+1]=i+1;
    a[1]=1,a[n+2]=n+2;
}
int main()
{
    n=read();
    for(int i=1;i<=n;i++) a[i]=read();
    discrete(); bldTr(rt,1,n+2);
    for(int i=2;i<=n+1;i++)
    {
        splay(i,rt); int x=siz[ch[rt][0]]+1;
        printf("%d ",x-1);
        split(i,x),rever(ch[ch[rt][1]][0]);
    }
    return 0;
}