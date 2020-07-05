/************************************************
 * Au: Hany01
 * Date: Aug 26th, 2018
 * Prob: LOJ2818 CF1012E EJOI2018
 * Email: hany01dxx@gmail.com & hany01@foxmail.com
 * Inst: Yali High School
************************************************/

#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
#define rep(i, j) for (register int i = 0, i##_end_ = (j); i < i##_end_; ++ i)
#define For(i, j, k) for (register int i = (j), i##_end_ = (k); i <= i##_end_; ++ i)
#define Fordown(i, j, k) for (register int i = (j), i##_end_ = (k); i >= i##_end_; -- i)
#define Set(a, b) memset(a, b, sizeof(a))
#define Cpy(a, b) memcpy(a, b, sizeof(a))
#define x first
#define y second
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)
#define SZ(a) ((int)(a).size())
#define ALL(a) a.begin(), a.end()
#define INF (0x3f3f3f3f)
#define INF1 (2139062143)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define y1 wozenmezhemecaia

template <typename T> inline bool chkmax(T &a, T b) { return a < b ? a = b, 1 : 0; }
template <typename T> inline bool chkmin(T &a, T b) { return b < a ? a = b, 1 : 0; }

inline int read() {
    static int _, __; static char c_;
    for (_ = 0, __ = 1, c_ = getchar(); c_ < '0' || c_ > '9'; c_ = getchar()) if (c_ == '-') __ = -1;
    for ( ; c_ >= '0' && c_ <= '9'; c_ = getchar()) _ = (_ << 1) + (_ << 3) + (c_ ^ 48);
    return _ * __;
}

const int maxn = 2e5 + 5;

int n, s, a[maxn], b[maxn], fa[maxn], fu, fv, p[maxn], stk[maxn], top, stk1[maxn], top1, vis[maxn], v[maxn], bk, tot, mgcir, num, las;
map<int, int> pos;

int find(int x) { return x == fa[x] ? x : fa[x] = find(fa[x]); }
inline void uni(int u, int v) { if ((u = find(u)) != (v = find(v))) fa[u] = v; }

int main()
{
#ifdef hany01
    freopen("loj2818.in", "r", stdin);
    freopen("loj2818.out", "w", stdout);
#endif

    n = read(), s = read();
    For(i, 1, n) a[i] = b[i] = read();
    sort(b + 1, b + 1 + n);
    Fordown(i, n, 1) pos[b[i]] = i;
    For(i, 1, n) fa[i] = i;
    For(i, 1, n) if (a[i] != b[i]) {
        while (a[pos[a[i]]] == b[pos[a[i]]]) ++ pos[a[i]];
        uni(i, pos[a[i]]), p[pos[a[i]]] = i, v[i] = pos[a[i]] ++, ++ tot;
    }
    if (tot > s) { puts("-1"); return 0; }

    For(i, 2, n) if (a[i] != b[i]) {
        if (las && b[i] == b[las]) {
            if ((fu = find(p[i])) != (fv = find(p[las])))
                swap(v[p[i]], v[p[las]]), fa[fu] = fv;
        } else las = i;
    }

    For(i, 1, n) if (!vis[i] && a[i] != b[i]) {
        int u = i;
        do vis[u] = 1, u = v[u]; while (u != i);
        ++ num;
    }
    Set(vis, 0);

    if (s == tot || s == tot + 1 || num <= 2) {
        printf("%d\n", num);
        For(i, 1, n) if (!vis[i] && a[i] != b[i]) {
            int u = i; top = 0;
            do stk[++ top] = u, vis[u] = 1, u = v[u]; while (u != i);
            printf("%d\n", top);
            For(j, 1, top) printf("%d ", stk[j]);
            putchar('\n');
        }
        return 0;
    }

    mgcir = min(s - tot, num), printf("%d\n", 2 + num - mgcir);
    For(i, 1, n) if (!vis[i] && a[i] != b[i]) {
        int u = i;
        do stk[++ top] = u, vis[u] = 1, u = v[u]; while (u != i);
        stk1[++ top1] = i;
        if (!-- mgcir) { bk = i; break; }
    }
    printf("%d\n", top);
    For(j, 1, top) printf("%d ", stk[j]);
    putchar('\n');
    printf("%d\n", top1);
    Fordown(j, top1, 1) printf("%d ", stk1[j]);
    putchar('\n');
    For(i, bk + 1, n) if (!vis[i] && a[i] != b[i]) {
        int u = i; top = 0;
        do stk[++ top] = u, vis[u] = 1, u = v[u]; while (u != i);
        printf("%d\n", top);
        For(j, 1, top) printf("%d ", stk[j]);
        putchar('\n');
    }

    return 0;
}
