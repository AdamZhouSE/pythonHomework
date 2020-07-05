#include <bits/stdc++.h>
#define Rint register int
#define mem(a, b) memset(a, (b), sizeof(a))
#define File(s) freopen(s ".in", "r", stdin), freopen(s ".out", "w", stdout)
#define For(i, j, k) for (Rint i = (j); i <= (k); i++)
#define Fordown(i, j, k) for (Rint i = (j); i >= (k); i--)

using namespace std;
typedef long long LL;

template <typename T>
inline void read(T &x) {
    x = 0;
    T w = 1, ch = getchar();
    while (!isdigit(ch)) {
        if (ch == '-')
            w = -1;
        ch = getchar();
    }
    while (isdigit(ch)) x = (x << 3) + (x << 1) + (ch ^ '0'), ch = getchar();
    x = x * w;
}

const int N = 2e5 + 10;
int n, S;
int a[N], b[N], fa[N], v[N], p[N], tot, num;
bool vis[N];
int stk[N], stk1[N], top, top1;
map<int, int> pos;

inline int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
inline void merge(int x, int y) {
    int fx = find(x), fy = find(y);
    if (fx != fy)
        fa[fx] = fy;
}
inline void init() { For(i, 1, n) fa[i] = i; }

int main() {
    read(n);
    read(S);
    init();
    For(i, 1, n) read(a[i]), b[i] = a[i];
    sort(b + 1, b + n + 1);
    Fordown(i, n, 1) pos[b[i]] = i;
    For(i, 1, n) if (a[i] != b[i]) {  // Init tot;
        int &pa = pos[a[i]];
        while (a[pa] == b[pa]) pa++;
        merge(i, pa);
        p[pa] = i;
        v[i] = pa;
        pa++;
        tot++;
    }
    if (tot > S) {
        printf("-1\n");
        return 0;
    }
    int las = 0;
    For(i, 1, n) if (a[i] != b[i]) {
        if (las && b[i] == b[las]) {
            int x = p[i], y = p[las], fx = find(x), fy = find(y);
            if (fx != fy)
                swap(v[x], v[y]), fa[fx] = fy;
        } else
            las = i;
    }
    For(i, 1, n) if (!vis[i] && a[i] != b[i]) {
        int x = i;
        do
            vis[x] = 1, x = v[x];
        while (x != i);
        ++num;
    }
    mem(vis, 0);
    if (S <= tot + 2 || num <= 2) {
        printf("%d\n", num);
        For(i, 1, n) if (!vis[i] && a[i] != b[i]) {
            int x = i;
            top = 0;
            do
                stk[++top] = x, vis[x] = 1, x = v[x];
            while (x != i);
            printf("%d\n", top);
            For(j, 1, top) printf("%d ", stk[j]);
            putchar('\n');
        }
        return 0;
    }
    int bkp, ext = min(S - tot, num);
    printf("%d\n", 2 + num - ext);
    For(i, 1, n) if (!vis[i] && a[i] != b[i]) {
        int x = i;
        do
            stk[++top] = x, vis[x] = 1, x = v[x];
        while (x != i);
        stk1[++top1] = i;
        --ext;
        if (!ext) {
            bkp = i;
            break;
        }
    }
    printf("%d\n", top);
    For(i, 1, top) printf("%d ", stk[i]);
    putchar('\n');
    printf("%d\n", top1);
    Fordown(i, top1, 1) printf("%d ", stk1[i]);
    putchar('\n');
    For(i, bkp + 1, n) if (!vis[i] && a[i] != b[i]) {
        int x = i;
        top = 0;
        do
            stk[++top] = x, vis[x] = 1, x = v[x];
        while (x != i);
        printf("%d\n", top);
        For(j, 1, top) printf("%d ", stk[j]);
        putchar('\n');
    }
    return 0;
}