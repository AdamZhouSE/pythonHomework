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