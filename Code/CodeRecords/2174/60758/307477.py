#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int, int>
char buf[1 << 20], *p1, *p2;
#define GC (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 20, stdin), p1 == p2) ? 0 : *p1++)
template <class T>
inline void read(T &n) {
    char ch = GC;
    T w = 1, x = 0;
    while (!isdigit(ch)) {
        if (ch == '-')
            w = -1;
        ch = GC;
    }
    while (isdigit(ch)) {
        x = (x << 3) + (x << 1) + (ch ^ 48);
        ch = GC;
    }
    n = x * w;
}
const int maxn = 100005;
int n, q, fa[maxn], size[maxn], st[maxn], top, cnt, tot, ans[maxn];
struct edge {
    int from, to, len, st, ed;
} E[maxn];
pii Q[maxn];
map<pii, int> Id;
inline int getfa(int x) {
    while (fa[x] != x) x = fa[x];
    return x;
}
inline void merge(int x, int y) {
    x = getfa(x);
    y = getfa(y);
    if (x == y)
        return;
    if (size[x] >= size[y]) {
        size[x] += size[y];
        fa[y] = x;
        st[++top] = y;
    } else {
        size[y] += size[x];
        fa[x] = y;
        st[++top] = x;
    }
}
inline void del(int x) {
    size[fa[x]] -= size[x];
    fa[x] = x;
}
struct segment_tree {
    int solved[maxn << 2];
    vector<int> e[maxn << 2];
    void insert(int l, int r, int id, int L, int R, int eg) {
        if (L > R)
            return;
        if (L <= l && r <= R) {
            e[id].push_back(eg);
            return;
        }
        int mid = (l + r) >> 1;
        if (L <= mid)
            insert(l, mid, id << 1, L, R, eg);
        if (R > mid)
            insert(mid + 1, r, id << 1 | 1, L, R, eg);
    }
    void solve(int l, int r, int id, int k) {
        if (solved[id])
            return;
        int flag = top;
        for (int i = 0; i < (int)e[id].size(); i++) merge(E[e[id][i]].from, E[e[id][i]].to);
        if (l < r) {
            int mid = (l + r) >> 1;
            solve(l, mid, id << 1, k);
            solve(mid + 1, r, id << 1 | 1, k);
            solved[id] = (solved[id << 1] & solved[id << 1 | 1]);
        } else if (ans[l] == -1 && getfa(Q[l].first) == getfa(Q[l].second))
            ans[l] = k, solved[id] = 1;
        while (top != flag) del(st[top--]);
    }
} T;
int main() {
    read(n);
    read(q);
    for (int i = 1, opt, x, y; i <= q; i++) {
        read(opt);
        if (!opt) {
            read(x);
            read(y);
            x++, y++;
            if (x > y)
                swap(x, y);
            tot++;
            E[tot].from = x;
            E[tot].to = y;
            read(E[tot].len);
            E[tot].st = cnt + 1;
            E[tot].ed = -1;
            Id[pii(x, y)] = tot;
        }
        if (opt == 1) {
            read(x);
            read(y);
            x++, y++;
            if (x > y)
                swap(x, y);
            int tmp = Id[pii(x, y)];
            E[tmp].ed = cnt;
        }
        if (opt == 2) {
            read(x);
            read(y);
            Q[++cnt] = pii(x + 1, y + 1);
        }
    }
    for (int i = 1; i <= tot; i++)
        if (E[i].ed == -1)
            E[i].ed = cnt;
    for (int i = 1; i <= n; i++) fa[i] = i, size[i] = 1;
    memset(ans, -1, sizeof(ans));
    for (int i = 0; i <= 9; i++) {
        for (int now = 1; now <= tot; now++)
            if (E[now].len == i)
                T.insert(1, cnt, 1, E[now].st, E[now].ed, now);
        T.solve(1, cnt, 1, i);
    }
    for (int i = 1; i <= cnt; i++) printf("%d\n", ans[i]);
    return 0;
}