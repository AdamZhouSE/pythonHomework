#include <cstdio>
#include <algorithm>
const int maxn = 100010;
int n, k;
struct edge {
    int to;
    edge* next;
} E[maxn * 2], *ne = E, *first[maxn];
void link(int u, int v) {
    *ne = (edge){ v, first[u] };
    first[u] = ne++;
}
int siz[maxn];
int getg(int i, int f) {
    siz[i] = 1;
    int g = -1;
    bool isg = 1;
    for (edge* e = first[i]; e; e = e->next)
        if (e->to != f) {
            int x = getg(e->to, i);
            if (x > -1)
                g = x;
            siz[i] += siz[e->to];
            if (siz[e->to] > n / 2)
                isg = 0;
        }
    if (n - siz[i] > n / 2)
        isg = 0;
    if (isg)
        g = i;
    return g;
}
int g, id[maxn], rt[maxn], list[maxn], rk[maxn], ssum[maxn], cnt;
bool cmp(int i, int j) { return siz[rt[i]] < siz[rt[j]]; }
void fil(int i, int f, int x) {
    id[i] = x;
    for (edge* e = first[i]; e; e = e->next)
        if (e->to != f)
            fil(e->to, i, x);
}
int check(int i) {
    if (i == g || cnt <= k)
        return 1;
    int s = ssum[cnt - k] + 1;
    if (rk[id[i]] >= cnt - k) {
        int t = ssum[cnt - k - 1] + siz[rt[id[i]]] - siz[i] + 1;
        if (t < s)
            s = t;
    } else
        s -= siz[i];
    return s <= n / 2;
}
int main() {
    scanf("%d%d", &n, &k);
    for (int i = 1, u, v; i < n; i++) scanf("%d%d", &u, &v), link(u, v), link(v, u);
    g = getg(1, 0);
    getg(g, 0);
    for (edge* e = first[g]; e; e = e->next) {
        fil(e->to, g, cnt);
        list[cnt] = cnt;
        rt[cnt++] = e->to;
    }
    std::sort(list, list + cnt, cmp);
    for (int i = 0; i < cnt; i++) {
        rk[list[i]] = i;
        ssum[i + 1] = ssum[i] + siz[rt[list[i]]];
    }
    for (int i = 1; i <= n; i++) printf("%d\n", check(i));
}