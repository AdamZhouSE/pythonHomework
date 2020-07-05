///Too difficult
#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define File(a) freopen(a".in", "r", stdin), freopen(a".out", "w", stdout)
#define rep(i, j) for (register int i = 0, i##_end_ = (j); i < i##_end_; ++ i)
#define For(i, j, k) for (register int i = (j), i##_end_ = (k); i <= i##_end_; ++ i)
#define Fordown(i, j, k) for (register int i = (j), i##_end_ = (k); i >= i##_end_; -- i)
#define Set(a, b) memset(a, b, sizeof(a))
#define Cpy(a, b) memcpy(a, b, sizeof(a))
#define x first
#define y second
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
#define INF (0x3f3f3f3f)
#define INF1 (2139062143)
#define debug(...) fprintf(stderr, __VA_ARGS__)

template <typename T> inline bool chkmax(T &a, T b) { return a < b ? a = b, 1 : 0; }
template <typename T> inline bool chkmin(T &a, T b) { return b < a ? a = b, 1 : 0; }

inline int read()
{
    register int _, __; register char c_;
    for (_ = 0, __ = 1, c_ = getchar(); c_ < '0' || c_ > '9'; c_ = getchar()) if (c_ == '-') __ = -1;
    for ( ; c_ >= '0' && c_ <= '9'; c_ = getchar()) _ = (_ << 1) + (_ << 3) + (c_ ^ 48);
    return _ * __;
}

const int maxn = 100005;

int n, m, cur, Ans[maxn], pos[maxn];
int ch[maxn << 1][2], fa[maxn << 1], len[maxn << 1], tot = 1, las = 1;
char s[maxn];

struct Question
{
    int l, r, id;
    bool operator < (const Question& A) const { return r != A.r ? r < A.r : l < A.l; }
}Q[maxn];

struct SegmentTree
{
    int tr[maxn << 4];

#define lc (t << 1)
#define rc (lc | 1)
#define mid ((l + r) >> 1)

    inline void update(int t, int l, int r, int x, int dt) {
        if (l == r) { chkmax(tr[t], dt); return; }
        if (x <= mid) update(lc, l, mid, x, dt);
        else update(rc, mid + 1, r, x, dt);
        tr[t] = max(tr[lc], tr[rc]);
    }

    inline int query(int t, int l, int r, int x, int y) {
        if (x <= l && r <= y) return tr[t];
        if (y <= mid) return query(lc, l, mid, x, y);
        if (x >  mid) return query(rc, mid + 1, r, x, y);
        return max(query(lc, l, mid, x, y), query(rc, mid + 1, r, x, y));
    }

#undef mid

}ST;

struct LCT
{
    int fa[maxn << 1], ch[maxn << 1][2], co[maxn << 1];

#define dir(u) (ch[fa[u]][1] == u)
#define isrt(u) (ch[fa[u]][1] != u && ch[fa[u]][0] != u)

    inline void pushdown(int u) { co[ch[u][0]] = co[ch[u][1]] = co[u]; }

    inline void rotate(int u) {
        int f = fa[u], gf = fa[f], d = dir(u);
        fa[ch[f][d] = ch[u][d ^ 1]] = f, fa[u] = gf;
        if (!isrt(f)) ch[gf][dir(f)] = u;
        ch[fa[f] = u][d ^ 1] = f;
    }

    int top, stk[maxn];
    inline void splay(int o) {
        stk[top = 1] = o;
        for (register int t = o; !isrt(t); t = fa[t]) stk[++ top] = fa[t];
        while (top) pushdown(stk[top --]);
        for ( ; !isrt(o); rotate(o)) if (!isrt(fa[o])) rotate(dir(o) == dir(fa[o]) ? fa[o] : o);
    }

    inline void access(int u, int id) {
        for (int t = 0; u; t = u, u = fa[u]) {
            splay(u);
            if (co[u]) ST.update(1, 1, n, co[u], len[u]);
            ch[u][1] = t, co[u] = id;
        }
    }

}lct;

inline void extend(int c, int id)
{
    int np = ++ tot, p = las;
    pos[id] = np;
    len[las = np] = len[p] + 1;
    while (p && !ch[p][c]) ch[p][c] = np, p = fa[p];
    if (!p) fa[np] = 1;
    else {
        int q = ch[p][c];
        if (len[q] == len[p] + 1) fa[np] = q;
        else {
            int nq = ++ tot;
            len[nq] = len[p] + 1, Cpy(ch[nq], ch[q]), fa[nq] = fa[q];
            fa[q] = fa[np] = nq;
            while (p && ch[p][c] == q) ch[p][c] = nq, p = fa[p];
        }
    }
}

int main()
{
#ifdef hany01
    File("loj6041");
#endif

    n = read(), m = read(), scanf("%s", s + 1);
    For(i, 1, m) Q[i].l = read(), Q[i].r = read(), Q[i].id = i;
    sort(Q + 1, Q + 1 + m), cur = 1;
    For(i, 1, n) extend(s[i] ^ 48, i);
    For(i, 1, tot) lct.fa[i] = fa[i];

    For(r, 1, n) {
        lct.access(pos[r], r);
        while (cur <= m && Q[cur].r == r)
            Ans[Q[cur].id] = ST.query(1, 1, n, Q[cur].l, Q[cur].r), ++ cur;
    }
    For(i, 1, m) printf("%d\n", Ans[i]);

    return 0;
}