
Luogu
应用 
 题库
 题单
 比赛
 讨论
  登录 注册 
洛谷 / 题目列表 / 题目详情 / 查看题解 
P2633 Count on a tree 题解
题目P2633 Count on a tree
总数量18 篇
以下题解仅供学习参考使用。
抄袭、复制题解，以达到刷AC率/AC数量或其他目的的行为，在洛谷是严格禁止的。

洛谷非常重视学术诚信。此类行为将会导致您成为作弊者。具体细则请查看洛谷社区规则。

评论
哦哟筷子
dalao tql
神奇的呆子
这个题解太棒了
并非圣人Oo
%%%
_风休住
捕捉楼上巨佬
gzn7264
捕捉楼上和楼上的楼上巨佬%%%
gzn7264
这个题解非常棒
ueettttuj
这个题解非常棒
子曰子悦
棒呆了
hater
tql
hacker_chen
捕捉4楼巨佬
作者: _风休住 更新时间: 2019-05-20 19:21  在Ta的博客查看 举报  17 
更佳阅读体验

这题不难呀，怎么调了这么久？ ——Mr. G

前置知识是主席树。在利用主席树求解区间第K小数时可以发现，主席树是一种类似前缀和的数据结构，具有和前缀和类似的区间加减及差分等优秀性质。在求解线性区间的第K小数时，我们需要将该区间内的所有数值信息扔到一棵主席树中，并在这棵主席树上左右递归，以找到第K小数；同样的，我们可以类比树上前缀和的操作，定义s[u]s[u]为从根节点到第uu号节点的“前缀主席树”（感性理解谢谢）。那么，包含uu到vv上所有数值信息的主席树就应该是：
s[u]+s[v]-s[lca(u,v)]-s[fa[lca(u,v)]]
s[u]+s[v]−s[lca(u,v)]−s[fa[lca(u,v)]]
理解上式后，问题基本可以解决了。另外注意离散化和主席树的代码细节。代码如下：

#include<bits/stdc++.h>
using namespace std;
// 离散化操作
#define id(x) (lower_bound(b+1,b+L+1,a[x])-b)
#define rid(x) (b[x])

const int MAXN = 100005;

struct Node {
    int l, r, sum;
}node[10000005];
int head[MAXN],cnt;

vector<int> G[MAXN];

int N, M, L, lastans;
int a[MAXN], b[MAXN];
int f[MAXN][19], dep[MAXN];

inline void build(Node &u, int l, int r) {
    u.sum = 0;
    if (l == r) return;
    int mid = (l + r) >> 1;
    build(node[u.l = ++cnt], l, mid);
    build(node[u.r = ++cnt], mid + 1, r);
}

inline void insert(Node c, Node &u, int l, int r, int p) {
    u.sum = c.sum + 1;
    if (l == r) return;
    int mid = (l + r) >> 1;
    if(p <= mid)
        insert(node[c.l], node[u.l = ++cnt], l, mid, p), u.r = c.r;
    else
        insert(node[c.r], node[u.r = ++cnt], mid+1, r, p), u.l = c.l;
}

inline void dfs(int u, int fa) {
    insert(node[head[fa]], node[head[u] = ++cnt], 1, L, id(u));
    f[u][0] = fa;
    dep[u] = dep[fa] + 1;
    for (register int i = 1; i <= 18; ++i)
        f[u][i] = f[f[u][i-1]][i-1];
    for (vector<int>::iterator it = G[u].begin(); it != G[u].end(); it++) {
        int v = *it;
        if (v == fa) continue;
        dfs(v, u);
    }
}

inline int Lca(int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    for (register int i = 18; i >= 0; --i) {
        if (dep[f[u][i]] >= dep[v]) u = f[u][i];
    }
    if (u == v) return u;
    for (register int i = 18; i >= 0; --i) {
        if (f[u][i] != f[v][i])
            u = f[u][i], v = f[v][i];
    }
    return f[u][0];
}

inline int query(Node x, Node y, Node z, Node w, int l, int r, int k) {
    if (l == r) return l;
    int sum = node[x.l].sum + node[y.l].sum - node[z.l].sum - node[w.l].sum;
    int mid = (l + r) >> 1;
    if(sum >= k) return query(node[x.l], node[y.l], node[z.l], node[w.l], l, mid, k);
    return query(node[x.r], node[y.r], node[z.r], node[w.r], mid+1, r, k - sum);
}

inline int querypath(int u, int v, int k) {
    int lca = Lca(u, v);
    return rid(query(node[head[u]], node[head[v]], node[head[lca]], node[head[f[lca][0]]], 1, L, k));
}

int main() {
    scanf("%d%d", &N, &M);
    for (register int i = 1; i <= N; ++i)
        scanf("%d", &a[i]), b[i] = a[i];
    for (register int i = 1; i < N; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        G[u].push_back(v);
        G[v].push_back(u);
    }
    sort(b + 1, b + N + 1);
    L = unique(b + 1, b + N + 1) - (b + 1);
    build(node[head[0] = ++cnt], 1, L);
    dfs(1, 0);
    for (register int i = 1; i <= M; ++i) {
        int u, v, k;
        scanf("%d%d%d", &u, &v, &k);
        int nowans = querypath(u^lastans, v, k);
        printf("%d\n", nowans);
        lastans = nowans;
    }
}
评论
SEELE
妈耶, query(lson[ql])中的lson指的是以ql为根的主席树中的lson,rson,而不是题目中的tree
SEELE
1~n是离散后的点权
SEELE
大家不要搞混
SEELE
%zykykyk
Dispwnl
。
Gypsophila
两个dfs真的好吗
KajKeusaka
树剖本来就两个DFS呀
wky32768
orzzyk
ecnerwaIa
这题彻底激怒我了，再RE，我就直接splay+主席树走起
ecnerwaIa
等会，好像splay不行，FHQ-treap可以
作者: 夏色祭 更新时间: 2018-01-04 20:34  在Ta的博客查看 举报  13 
主席树板子题啊。。。

只是把序列的操作改成了树上。。。

序列的主席树维护的是[1-i]这里维护从1到i的这条路径上的结点的值。

查询就套个树上差分：v[ql]+v[qr]-v[lca]-v[lca_fa]。

lca的话再套个树剖lca就行了。

是不是很简单。。。

代码：

#include<cstdio>
#include<algorithm>
#include<string>
#define For(i,x,y) for (int i=x;i<=y;i++)
#define cross(i,k) for (int i=first[k];i;i=last[i])
#define N 100010
#define il inline
#define vd void
using namespace std;
struct node{
    int num,v;
}a[N];
int rt[N],v[N*20],lson[N*20],rson[N*20],to[N<<1],last[N<<1],first[N],b[N],rk[N];
int n,m,x,y,k,tot,cnt,lastans,lca;
il int read(){
    int x=0;int ch=getchar(),f=1;
    while (!isdigit(ch)&&(ch!='-')&&(ch!=EOF)) ch=getchar();
    if (ch=='-'){f=-1;ch=getchar();}
    while (isdigit(ch)){x=(x<<1)+(x<<3)+ch-'0';ch=getchar();}
    return x*f;
}
il bool cmp(node x,node y){return x.v<y.v;}
il vd add(int x,int y){to[++tot]=y,last[tot]=first[x],first[x]=tot;}
il vd insert(int &u,int last,int l,int r,int k){
    u=++cnt,v[u]=v[last]+1;
    if (l==r) return;
    lson[u]=lson[last],rson[u]=rson[last];
    int mid=l+r >> 1;
    if (k<=mid) insert(lson[u],lson[u],l,mid,k);
        else insert(rson[u],rson[u],mid+1,r,k);
}//插入

int size[N],son[N],fa[N],dep[N];
il vd dfs(int k){
    size[k]=1,dep[k]=dep[fa[k]]+1;
    insert(rt[k],rt[fa[k]],1,n,b[k]);
    cross(i,k){
        int v=to[i];
        if (v==fa[k]) continue;
        fa[v]=k,dfs(v);
        size[k]+=size[v];
        if (!son[k]||size[v]>size[son[k]]) son[k]=v;
    }
}
int top[N];
il vd dfs(int k,int tp){
    top[k]=tp;
    if (!son[k]) return;
    dfs(son[k],tp);
    cross(i,k){
        int v=to[i];
        if (v==son[k]||v==fa[k]) continue;
        dfs(v,v);
    }
}
il int Lca(int x,int y){
    while (top[x]!=top[y])
        if (dep[top[x]]>=dep[top[y]]) x=fa[top[x]];
            else y=fa[top[y]];
    if (dep[x]>=dep[y]) return y;
        else return x; 
}//树剖lca il int query(int ql,int qr,int lca,int lca_fa,int l,int r,int k){

    if (l==r) return l;
    int mid=l+r >> 1,t=v[lson[ql]]+v[lson[qr]]-v[lson[lca]]-v[lson[lca_fa]];
    if (t>=k) return query(lson[ql],lson[qr],lson[lca],lson[lca_fa],l,mid,k);
        else return query(rson[ql],rson[qr],rson[lca],rson[lca_fa],mid+1,r,k-t);
}//查询

int main(){
    n=read(),m=read();
    For(i,1,n){
        b[i]=read();
        a[i].num=i,a[i].v=b[i];
    }
    sort(a+1,a+1+n,cmp),a[0].v=-233333333;
    For(i,1,n)
        if (a[i].v!=a[i-1].v) rk[++x]=b[a[i].num],b[a[i].num]=x;
            else b[a[i].num]=x;//离散
    For(i,1,n-1){
        x=read(),y=read();
        add(x,y),add(y,x);
    }
    dfs(1);
    dfs(1,1);
    For(i,1,m){
        x=read(),y=read(),k=read();
        x^=lastans,lca=Lca(x,y);
        lastans=rk[query(rt[x],rt[y],rt[lca],rt[fa[lca]],1,n,k)];
        printf("%d\n",lastans);
    }
    return 0;
}
评论
Hygebra
敲喜欢这个码风
作者: 花淇淋 更新时间: 2017-05-21 21:52  在Ta的博客查看 举报  7 
第一步：离散化

即：把节点的点权换成它在所有点权中的排名（它是第几小的）

将存储点权的数组复制一份之后排序，去重，然后将原先的每个点权在去重后的数组里进行二分查找，就可以得到它的排名。

第二步：建主席树

每个节点维护它到根的路径上的权值线段树，所以每个节点可以利用它的父节点更新，所以将整棵树dfs一遍，在此过程中建树。

第三步：求解

用u点的主席树+v点的主席树-lca(u,v)的主席树-lca(u,v)父节点的主席树，在这样产生的主席树上查找第k小的排名，最后输出它原来的点权。

代码如下

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;
const int e=1e5+5;
struct point
{
    int l,r,w;
}c[e*30];
int fa[e][21],a[e],h[e],tot,num,deep[e],n,m,rt[e],xxx,val[e];
int next[e<<1],head[e],go[e<<1];
inline int read()
{
    char ch;
    int res=0;
    bool f=false;
    while(ch=getchar(),(ch<'0'||ch>'9')&&ch!='-');
    if(ch=='-')f=true;
    else res=ch-48;
    while(ch=getchar(),ch>='0'&&ch<='9')
    res=(res<<3)+(res<<1)+ch-48;
    return f? -res:res;
}
inline void insert(int y,int &x,int l,int r,int p)
{
    c[x=++num]=c[y];
    c[x].w++;
    if(l==r)return;
    int mid=l+r>>1;
    if(p<=mid)insert(c[y].l,c[x].l,l,mid,p);
    else insert(c[y].r,c[x].r,mid+1,r,p);
    c[x].w=c[c[x].l].w+c[c[x].r].w;
}
inline int query(int x,int y,int z,int d,int l,int r,int k)
{
    if(l==r)return l;
    int ret=c[c[x].l].w+c[c[y].l].w-c[c[z].l].w-c[c[d].l].w;
    int mid=l+r>>1;
    if(k<=ret)
    return query(c[x].l,c[y].l,c[z].l,c[d].l,l,mid,k);
    else return query(c[x].r,c[y].r,c[z].r,c[d].r,mid+1,r,k-ret);
}
inline void add(int x,int y)
{
    next[++tot]=head[x];
    head[x]=tot;
    go[tot]=y;
    next[++tot]=head[y];
    head[y]=tot;
    go[tot]=x;
}
inline void dfs2(int u)
{
    insert(rt[fa[u][0]],rt[u],1,n,val[u]);
    for(int i=head[u];i;i=next[i])
    {
        int v=go[i];
        if(v==fa[u][0])continue;
        dfs2(v);
    }
}
inline void dfs(int u,int father)
{
    deep[u]=deep[father]+1;
    for(int i=0;i<=19;i++)
    fa[u][i+1]=fa[fa[u][i]][i];
    for(int i=head[u];i;i=next[i])
    {
        int v=go[i];
        if(v==father)continue;
        fa[v][0]=u;
        dfs(v,u);
    }
}
inline int lca(int x,int y)
{
    if(deep[x]<deep[y])swap(x,y);
    for(int i=19;i>=0;i--)
    {
        if(deep[fa[x][i]]>=deep[y])
        x=fa[x][i];
        if(x==y)return x;
    }
    for(int i=19;i>=0;i--)
    {
        if(fa[x][i]!=fa[y][i])
        {
            x=fa[x][i];
            y=fa[y][i];
        }
    }
    return fa[x][0];
}
inline int find(int x)
{
    int l=1,r=xxx,mid;
    while(l<=r)
    {
        mid=l+r>>1;
        if(x>h[mid])
        l=mid+1;
        else r=mid-1;
    }
    return l;
}
int main()
{
    int i,j,u,v,k;
    n=read();
    m=read();
    for(i=1;i<=n;i++)
    {
        val[i]=read();
        a[i]=val[i];
    }
    for(i=1;i<n;i++)
    {
        u=read();
        v=read();
        add(u,v);
    }
    sort(a+1,a+n+1);
    h[1]=a[1];
    xxx=1;
    for(i=2;i<=n;i++)
    if(a[i]!=a[i-1])h[++xxx]=a[i];
    for(i=1;i<=n;i++)
    val[i]=find(val[i]);
    dfs(1,0);
    int ans=0;
    dfs2(1);
    for(i=1;i<=m;i++)
    {
        u=read();
        v=read();
        k=read();
        u^=ans;
        int z=lca(u,v);
        int last=query(rt[u],rt[v],rt[z],rt[fa[z][0]],1,n,k);
        ans=h[last];
        printf("%d",ans);
        if(i!=m)putchar('\n');
    }
    return 0;
}
评论
chrysanthemum
写下你的评论...
行者_Walker
写下你的评论...
Hattori
写下你的评论…
diu·
写下你的评论…
Isaunoya
树剖%%%
G2022TNT
写下你的评论...
作者: alpha1022  更新时间: 2018-11-13 13:09  在Ta的博客查看 举报  4 
第 K 大？主席树！

考虑树上静态求路径信息（具有区间减法性质）：
s_x + s_y - s_{lca} - s_{fa_{lca}}s 
x
​	 +s 
y
​	 −s 
lca
​	 −s 
fa 
lca
​	 
​	 ，其中 s_xs 
x
​	  表示结点 xx 到根的信息。

那么扩展到主席树即可。

注意离散化！

注意重复元素！我就是因为这一点在 BZOJ RE，SPOJ 原题 WA 的，不过洛谷数据没有重复的。

代码：

#include <cstdio>
#include <algorithm>
using namespace std;

const int BUFF_SIZE = 1 << 20;
char BUFF[BUFF_SIZE],*BB,*BE;
#define gc() (BB == BE ? (BE = (BB = BUFF) + fread(BUFF,1,BUFF_SIZE,stdin),BB == BE ? EOF : *BB++) : *BB++)
template<class T>
inline void read(T &x)
{
    x = 0;
    char ch = 0,w = 0;
    while(ch < '0' | ch > '9')
        w |= ch == '-',ch = gc();
    while(ch >= '0' && ch <= '9')
        x = (x << 3) + (x << 1) + (ch ^ '0'),ch = gc();
    w ? x = -x : x;
}

#define ls(p) seg[p].lson
#define rs(p) seg[p].rson
#define cnt(p) seg[p].cnt
const int N = 1e5;
long long lastans;
int n,m,rt[N + 10],len;
long long a[N + 10],ind[N + 10];
int to[(N << 1) + 10],pre[(N << 1) + 10],first[N + 10];
inline void add(int u,int v)
{
    static int tot = 0;
    to[++tot] = v;
    pre[tot] = first[u];
    first[u] = tot;
}
struct segnode
{
    int cnt,lson,rson;
} seg[(N << 5) + 10];
int insert(int x,int tl,int tr,int p)
{
    static int tot = 0;
    int cur = ++tot;
    seg[cur] = seg[p];
    if(tl == tr)
    {
        ++cnt(cur);
        return cur;
    }
    int mid = tl + tr >> 1;
    if(x <= mid)
        ls(cur) = insert(x,tl,mid,ls(cur));
    else
        rs(cur) = insert(x,mid + 1,tr,rs(cur));
    cnt(cur) = cnt(ls(cur)) + cnt(rs(cur));
    return cur;
}
int query(int k,int tl,int tr,int x,int y,int lca,int fa_lca)
{
    if(tl == tr)
        return tl;
    int mid = tl + tr >> 1;
    int cnt = cnt(ls(x)) + cnt(ls(y)) - cnt(ls(lca)) - cnt(ls(fa_lca));
    if(k <= cnt)
        return query(k,tl,mid,ls(x),ls(y),ls(lca),ls(fa_lca));
    else
        return query(k - cnt,mid + 1,tr,rs(x),rs(y),rs(lca),rs(fa_lca));
}
int fa[N + 10],dep[N + 10],sz[N + 10],son[N + 10],top[N + 10];
int q[N + 10],head,tail;
inline int getlca(int x,int y)
{
    while(top[x] ^ top[y])
        dep[top[x]] > dep[top[y]] ? x = fa[top[x]] : y = fa[top[y]];
    return dep[x] < dep[y] ? x : y;
}
int main()
{
    read(n),read(m);
    for(register int i = 1;i <= n;++i)
        read(a[i]),ind[i] = a[i];
    sort(ind + 1,ind + n + 1);
    len = unique(ind + 1,ind + n + 1) - ind - 1;
    for(register int i = 1;i <= n;++i)
        a[i] = lower_bound(ind + 1,ind + len + 1,a[i]) - ind;
    int u,v;
    for(register int i = 1;i < n;++i)
        read(u),read(v),add(u,v),add(v,u);
    rt[1] = insert(a[1],1,n,0);
    q[++tail] = dep[1] = 1;
    while(head < tail)
    {
        int p = q[++head];
        for(register int i = first[p];i;i = pre[i])
            if(to[i] ^ fa[p])
            {
                fa[to[i]] = p;
                dep[to[i]] = dep[p] + 1;
                rt[to[i]] = insert(a[to[i]],1,n,rt[p]);
                q[++tail] = to[i];
            }
    }
    for(register int i = n;i;--i)
    {
        sz[fa[q[i]]] += sz[q[i]];
        if(!son[fa[q[i]]] || sz[q[i]] > sz[son[fa[q[i]]]])
            son[fa[q[i]]] = q[i];
    }
    for(register int i = 1;i <= n;++i)
        top[q[i]] = son[fa[q[i]]] == q[i] ? top[fa[q[i]]] : q[i];
    int x,y,k,lca;
    while(m--)
    {
        read(x),read(y),read(k);
        x ^= lastans;
        lca = getlca(x,y);
        printf("%lld\n",lastans = ind[query(k,1,n,rt[x],rt[y],rt[lca],rt[fa[lca]])]);
    }
    return 0;
}
评论
zxyoi
ykdalao%%%%%
yasuolol
您好，离散化数量还应该多-1吧？
光明正大
英爱不用减一吧
作者: dream_maker  更新时间: 2018-05-13 13:59  在Ta的博客查看 举报  4 
P2633 Count on a tree

题目描述

给定一棵N个节点的树，每个点有一个权值，对于M个询问(u,v,k)，你需要回答u xor lastans和v这两个节点间第K小的点权。其中lastans是上一个询问的答案，初始为0，即第一个询问的u是明文。

输入格式： 第一行两个整数N,M。 第二行有N个整数，其中第i个整数表示点i的权值。 后面N-1行每行两个整数(x,y)，表示点x到点y有一条边。 最后M行每行两个整数(u,v,k)，表示一组询问。

输出格式： M行，表示每个询问的答案。

输入样例： 8 5 105 2 9 3 8 5 7 7 1 2 1 3 1 4 3 5 3 6 3 7 4 8 2 5 1 0 5 2 10 5 3 11 5 4 110 8 2

输出样例： 2 8 9 105 7 说明 N,M<=100000

一道不错(毒瘤)的主席树练习题，因为主席树保存的是前缀和，这道题的题目框架是树形的，所以我们把一般的线性关系的主席树变成树形关系，再进行权值线段树的持久化就可以了。又因为对于两个节点(u,v)(u,v)，u到v路径上的数字个数可以表示成siz[u]+siz[v]-siz[lca(u,v)]-siz[fa[lca(u,v)]]siz[u]+siz[v]−siz[lca(u,v)]−siz[fa[lca(u,v)]]，根据这个性质我们就可以进行权值线段树上的二分了，注意书写细节即可(数组开小了)。

/*dream_maker*/
#include<bits/stdc++.h>
using namespace std;
#define N 100010
#define M 2000010
int read(){
    int ans=0,w=1;char c=getchar();
    while(c!='-'&&!isdigit(c))c=getchar();
    if(c=='-')w=-1,c=getchar();
    while(isdigit(c))ans=ans*10+c-'0',c=getchar();
    return ans*w;
}
int n,m,s,lastans=0,u,v,tot,cnt;
struct Edge{int v,next;}E[N<<1];
int head[N],a[N],b[N],fa[N][32],dep[N];
int rt[M]={0},ls[M]={0},rs[M]={0},siz[M]={0};
void add(int u,int v){
    E[++tot]=(Edge){v,head[u]};
    head[u]=tot;
}
void modify(int &rt,int lastrt,int l,int r,int val){
    if(!rt)rt=++cnt;
    if(l==r){siz[rt]++;return;}
    int mid=(l+r)>>1;
    if(mid>=val)modify(ls[rt],ls[lastrt],l,mid,val),rs[rt]=rs[lastrt];
    else modify(rs[rt],rs[lastrt],mid+1,r,val),ls[rt]=ls[lastrt];
    siz[rt]=siz[ls[rt]]+siz[rs[rt]];
}
int query(int rt1,int rt2,int rt3,int rt4,int l,int r,int k){
    if(l==r)return l;
    int mid=(l+r)>>1;
    int tmp=siz[ls[rt1]]+siz[ls[rt2]]-siz[ls[rt3]]-siz[ls[rt4]];
    if(tmp>=k)return query(ls[rt1],ls[rt2],ls[rt3],ls[rt4],l,mid,k);
    else return query(rs[rt1],rs[rt2],rs[rt3],rs[rt4],mid+1,r,k-tmp);
}
void dfs(int u,int f){
    dep[u]=dep[f]+1;
    for(int i=head[u];i;i=E[i].next){
        int v=E[i].v;
        if(v==fa[u][0])continue;
        fa[v][0]=u;
        modify(rt[v],rt[u],1,s,a[v]);
        dfs(v,u);
    }
}
int Lca(int x,int y){
    if(dep[x]<dep[y])swap(x,y);
    int t=dep[x]-dep[y];
    for(int i=0;(1<<i)<=t;i++)
        if((1<<i)&t)x=fa[x][i];
    for(int i=19;i>=0;i--)
        if(fa[x][i]!=fa[y][i])
            x=fa[x][i],y=fa[y][i];
    if(x==y)return x;
    return fa[x][0];
}
int main(){
    n=read();m=read();
    for(int i=1;i<=n;i++)b[i]=a[i]=read();
    sort(b+1,b+n+1);
    s=unique(b+1,b+n+1)-b;
    for(int i=1;i<n;i++){
        u=read();v=read();
        add(u,v);add(v,u);
    }
    for(int i=1;i<=n;i++)a[i]=lower_bound(b+1,b+s+1,a[i])-b;
    modify(rt[1],rt[0],1,s,a[1]);
    dfs(1,0);
    int up=log2(n);
    for(int k=1;k<=up;k++)
        for(int i=1;i<=n;i++)
            fa[i][k]=fa[fa[i][k-1]][k-1];
    for(int i=1;i<=m;i++){
        u=read();v=read();int k=read();
        u^=lastans;
        int lca=Lca(u,v);
        int ans=b[query(rt[u],rt[v],rt[lca],rt[fa[lca][0]],1,s,k)];
        printf("%d\n",ans);
        lastans=ans;
    }
    return 0;
}
 
1
2
3
4
>

在洛谷，
享受Coding的欢乐

关于洛谷 | 帮助中心 | 用户协议 | 联系我们
小黑屋 | 陶片放逐 | 社区规则 | 招贤纳才
2013-2020 , © 洛谷 Developed by the Luogu Dev Team
沪ICP备18008322号 All rights reserved.