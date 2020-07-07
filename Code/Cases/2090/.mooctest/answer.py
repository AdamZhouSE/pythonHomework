#include <bits/stdc++.h>
#define ll long long
#define pli pair<ll, int>
#define mp make_pair
using namespace std;
const int maxn = 100000 + 10;
int n, L, fa[maxn], q[maxn], cnt, que[maxn], l, r, head[maxn], tot;
ll dis[maxn], pre[maxn], down[maxn], sufmx[maxn][2], mx[2][2];
pli s1[maxn], s2[maxn];

inline int read() {
    register int x = 0, f = 1;
    char ch = getchar();
    for (; !isdigit(ch); ch = getchar())
        if (ch == '-')
            f = -1;
    for (; isdigit(ch); ch = getchar()) x = (x << 3) + (x << 1) + ch - '0';
    return (f == 1) ? x : -x;
}

struct node {
    int to, next, val;
} e[maxn << 1];

inline void addedge(int x, int y, int w) {
    e[++tot].to = y;
    e[tot].val = w;
    e[tot].next = head[x];
    head[x] = tot;
}
inline void clear() {
    for (; r; r--) dis[que[r]] = -1;
}
inline int bfs(int s) {
    int mx = 0;
    dis[s] = fa[s] = 0;
    que[l = r = 1] = s;
    while (l <= r) {
        int u = que[l++];
        if (dis[u] > dis[mx])
            mx = u;
        for (int i = head[u]; i; i = e[i].next) {
            int v = e[i].to;
            if (dis[v] == -1) {
                dis[v] = dis[u] + e[i].val;
                fa[v] = u;
                que[++r] = v;
            }
        }
    }
    return mx;
}
/*
(i < j)
1. down[i] - pre[i] + down[j] + pre[j] <= mid
2. down[i] + |pre[i] - pre[a]| + down[j] + |pre[j] - pre[b]| + L <=mid

2.(two pointers)
lim1 = down[i] + pre[i] + down[j] + pre[j] + L - mid <= pre[a] + pre[b]
lim2 = down[i] + pre[i] + down[j] - pre[j] + L - mid <= pre[a] - pre[b]
lim3 = down[i] - pre[i] + down[j] + pre[j] + L - mid <= - pre[a] + pre[b]
lim4 = down[i] - pre[i] + down[j] - pre[j] + L - mid <= - pre[a] - pre[b]

lim1 <= pre[a] + pre[b] b--;
lim3 <= - pre[a] + pre[b] b++;
lim2 <= pre[a] - pre[b]
lim4 <= - pre[a] - pre[b]
*/
inline bool check(ll mid) {
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) mx[i][j] = -1e18;
    for (int i = 1, j = 1; i <= cnt; i++) {
        while (j <= cnt && s1[j].first + s2[i].first <= mid) j++;
        for (int x = 0; x < 2; x++)
            for (int y = 0; y < 2; y++)
                mx[x][y] = max(mx[x][y],
                               down[s2[i].second] + (x ? -1 : 1) * pre[s2[i].second] + sufmx[j][y] + L - mid);
    }
    int p = 1, q = cnt + 1;
    for (int i = 1; i <= cnt; i++) {
        while (p <= cnt && pre[p] - pre[i] < mx[1][0]) p++;
        while (q > p && pre[i] + pre[q - 1] >= mx[0][0]) q--;
        int j = max(p, q);
        if (j <= cnt && pre[i] - pre[j] >= mx[0][1] && -pre[i] - pre[j] >= mx[1][1])
            return 1;
    }
    return 0;
}
inline bool cmp(const pli &a, const pli &b) { return a.first > b.first; }

int main() {
    memset(dis, -1, sizeof(dis));
    while (1) {
        n = read(), L = read();
        if (!n && !L)
            break;
        int x, y, w;
        for (int i = 1; i < n; i++) {
            x = read(), y = read(), w = read();
            addedge(x, y, w), addedge(y, x, w);
        }
        int s = bfs(1);
        clear();
        for (int t = bfs(s); t; t = fa[t]) q[++cnt] = t;
        reverse(q + 1, q + cnt + 1);
        for (int i = 1; i <= cnt; i++) pre[i] = dis[q[i]];
        ll l = 0, r = dis[q[cnt]], mid, ans = 1e18;
        clear();
        for (int i = 1; i <= cnt; i++) {
            dis[q[i - 1]] = dis[q[i + 1]] = 0;
            x = bfs(q[i]);
            down[i] = dis[x];
            clear();
            l = max(l, dis[bfs(x)]);
            clear();
            dis[q[i - 1]] = dis[q[i + 1]] = -1;
        }
        for (int i = 1; i <= cnt; i++) {
            s1[i] = mp(down[i] + pre[i], i);
            s2[i] = mp(down[i] - pre[i], i);
        }
        sort(s1 + 1, s1 + cnt + 1);
        sort(s2 + 1, s2 + cnt + 1, cmp);
        sufmx[cnt + 1][0] = sufmx[cnt + 1][1] = -1e18;
        for (int i = cnt; i; i--)
            for (int j = 0; j < 2; j++)
                sufmx[i][j] = max(sufmx[i + 1][j], down[s1[i].second] + (j ? -1 : 1) * pre[s1[i].second]);
        while (l <= r) {
            mid = (l + r) >> 1;
            if (check(mid))
                r = mid - 1, ans = mid;
            else
                l = mid + 1;
        }
        printf("%lld\n", ans);
        for (int i = 1; i <= n; i++) head[i] = 0;
        tot = cnt = 0;
    }
    return 0;
}