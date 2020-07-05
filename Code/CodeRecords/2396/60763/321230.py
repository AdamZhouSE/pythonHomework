#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#define re register
#define maxn 1000007
#define ll long long
#define ls rt<<1
#define rs rt<<1|1
#define inf 1000000007
using namespace std;
int ch[100001][2],f[maxn],cnt[maxn],key[maxn],size[maxn],mark[maxn],root,sz,data[maxn];
struct po
{
    int id,k;
}a[maxn];
inline int read()
{
    int x=0,c=1;
    char ch=' ';
    while((ch>'9'||ch<'0')&&ch!='-')ch=getchar();
    while(ch=='-')c*=-1,ch=getchar();
    while(ch<='9'&&ch>='0')x=x*10+ch-'0',ch=getchar();
    return x*c;
}
bool cmp(po x,po y)
{
    if(x.k<y.k)
    return 1;
    else if(x.k==y.k)
    return x.id<y.id;
    return 0;
}
inline int get(int x)
{
    return ch[f[x]][1]==x;
}
inline void update(int x)
{
    size[x]=size[ch[x][1]]+size[ch[x][0]]+1;
}
inline void pushdown(int x)
{
    if(mark[x]){
        if(ch[x][0]) mark[ch[x][0]]^=1;
        if(ch[x][1]) mark[ch[x][1]]^=1;
        swap(ch[x][0],ch[x][1]);
        mark[x]=0;
    }
}
inline void rotate(int x)
{
    int y=f[x],z=f[y];
    int kind=get(x);
    pushdown(y);pushdown(x);
    ch[y][kind]=ch[x][kind^1];f[ch[y][kind]]=y;
    ch[x][kind^1]=y;f[y]=x;f[x]=z;
    if(z){
        ch[z][ch[z][1]==y]=x;
    }
    update(y);update(x);
}
inline void splay(int x,int tar)
{
    for(re int fa;(fa=f[x])!=tar;rotate(x)){
        pushdown(f[fa]);pushdown(fa);pushdown(x);
        if(f[fa]!=tar)
            rotate(get(x)==get(fa)?fa:x);
    }
    if(!tar) root=x;
}
inline void build(int l,int r,int fa)
{
   if(l>r) return;
    int mid=l+r>>1;
    if(mid<fa) ch[fa][0]=mid;
    else ch[fa][1]=mid;
    size[mid]=1;f[mid]=fa;
    if(l==r) return;
    build(l,mid-1,mid);
    build(mid+1,r,mid);
    update(mid);
}
inline int findx(int x)
{
    int now=root;
    while(1){
        if(mark[now])
        pushdown(now);
        if(x<=size[ch[now][0]]&&ch[now][0])
        now=ch[now][0];
        else {
            x-=size[ch[now][0]]+1;
            if(x==0) return now;
            else now=ch[now][1];
        }
    }
}
int main()
{
    int n;
    cin>>n;
    for(re int i=2;i<=n+1;i++){
        a[i].k=read();
        a[i].id=i;
    }
    a[1].id=1,a[1].k=-inf;
    a[n+2].id=n+2,a[n+2].k=inf;
    sort(a+1,a+n+3,cmp);
    build(1,n+2,0);
    root=n+3>>1;
    for(re int i=2;i<=n;i++){
        splay(a[i].id,0);
        int ans=size[ch[root][0]]+1;
        printf("%d ",ans-1);
        int x1=findx(i-1);
        int y1=findx(ans+1);
        splay(x1,0);splay(y1,x1);
        mark[ch[ch[root][1]][0]]^=1;
    }
    cout<<n<< " ";
}