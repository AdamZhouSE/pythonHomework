#include<cstdio>
#include<algorithm> 
#include<cstring>
#include<vector>
#define LL long long
using namespace std;
const int N=1e5+5;
int n,m,r,last,size,root;
int p[N],mx[N],ans[N],num[N];
int c[N*2][2],fa[N*2],v[N*2],tag[N*2];
char s[N];
vector<int> q[N];
struct sam{int mx,fa,ch[2];}t[N*2];
int read()
{
    int x=0,f=1;char c=getchar();
    while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}
    while(c>='0'&&c<='9'){x=x*10+c-'0';c=getchar();}
    return x*f;
}
int lowbit(int x){return x&(-x);}
void modify(int x,int v){x=n-x+1;while(x<=n)mx[x]=max(mx[x],v),x+=lowbit(x);}
int query(int x){x=n-x+1;int ans=0;while(x)ans=max(ans,mx[x]),x-=lowbit(x);return ans;}
void ins(int c,int id)
{
    int np=++size;num[id]=np;
    t[np].mx=t[last].mx+1;
    int x=last;last=np;
    while(x&&!t[x].ch[c])t[x].ch[c]=np,x=t[x].fa;
    if(!x)t[np].fa=root;
    else
    {
        int y=t[x].ch[c];
        if(t[y].mx==t[x].mx+1)t[np].fa=y;
        else
        {
            int nq=++size;
            t[nq]=t[y];t[nq].mx=t[x].mx+1;
            t[y].fa=t[np].fa=nq;
            while(x&&t[x].ch[c]==y)t[x].ch[c]=nq,x=t[x].fa;
        }
    }
}
bool isroot(int x){return c[fa[x]][0]!=x&&c[fa[x]][1]!=x;}
void change(int x,int val){v[x]=tag[x]=val;}
void down(int x)
{
    if(!tag[x])return;
    if(c[x][0])change(c[x][0],tag[x]);
    if(c[x][1])change(c[x][1],tag[x]);
    tag[x]=0;
}
void rotate(int x)
{
    int y=fa[x],z=fa[y],l,r;
    if(c[y][0]==x)l=0;else l=1;r=l^1;
    if(!isroot(y)){if(c[z][0]==y)c[z][0]=x;else c[z][1]=x;}
    fa[x]=z;fa[y]=x;fa[c[x][r]]=y;
    c[y][l]=c[x][r];c[x][r]=y;
}
void relax(int x){if(!isroot(x))relax(fa[x]);down(x);}
void splay(int x)
{
    relax(x);
    while(!isroot(x))
    {
        int y=fa[x],z=fa[y];
        if(!isroot(y))
        {
            if((c[y][0]==x)^(c[z][0]==y))rotate(x);
            else rotate(y);
        }
        rotate(x);
    }
}
void access(int x,int val)
{
    int o=0;
    while(x)
    {
        splay(x);modify(v[x],t[x].mx);
        c[x][1]=o;o=x;x=fa[x];
    }
    tag[o]=v[o]=val;
}
void build(){for(int i=1;i<=size;i++)fa[i]=t[i].fa;}
int main()
{
    n=read();m=read();
    scanf("%s",s+1);
    for(int i=1;i<=m;i++)
    {
        p[i]=read();r=read();
        q[r].push_back(i);
    }
    last=size=root=1;
    for(int i=1;i<=n;i++)ins(s[i]-'0',i);
    build();
    for(int i=1;i<=n;i++)
    {
        access(num[i],i);
        int sz=q[i].size();
        for(int j=0;j<sz;j++)
        {
            int x=q[i][j];
            ans[x]=query(p[x]);
        }
    }
    for(int i=1;i<=m;i++)printf("%d\n",ans[i]);
    return 0;
}