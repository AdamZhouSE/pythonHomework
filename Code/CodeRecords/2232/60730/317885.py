#include <bits/stdc++.h>

using namespace std;

const int N = 110, M = N * N;

int n;
int h[N], e[M], ne[M], idx;
int dfn[N], low[N], timestamp;
int stk[N], tt;
bool in_stk[N];
int id[N], sz[N], scc_cnt;
int din[N], dout[N];

void add(int a, int b) {
    e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}

void tarjan(int u) {
    dfn[u] = low[u] = ++timestamp;
    stk[++tt] = u, in_stk[u] = true;
    for (int i = h[u]; ~i; i = ne[i]) {
        int j = e[i];
        if (!dfn[j]) {
            tarjan(j);
            low[u] = min(low[u], low[j]);
        } else if (in_stk[j]) {
            low[u] = min(low[u], dfn[j]);
        }
    }
    if (dfn[u] == low[u]) {
        ++scc_cnt;
        int v;
        do {
            v = stk[tt--];
            in_stk[v] = false;
            id[v] = scc_cnt;
            sz[scc_cnt]++;
        } while (v != u);
    }
} 

int main() {
    cin >> n;
    memset(h, -1, sizeof h);
    for (int i = 1; i <= n; i++) {
        int t;
        while (cin >> t, t) add(i, t);
    }
    for (int i = 1; i <= n; i++) {
        if (!dfn[i]) tarjan(i);
    }
    for (int i = 1; i <= n; i++) {
        for (int j = h[i]; ~j; j = ne[j]) {
            int k = e[j];
            int a = id[i], b = id[k];
            if (a != b) dout[a]++, din[b]++;
        }
    }
    int src = 0, des = 0;
    for (int i = 1; i <= scc_cnt; i++) {
        if (!din[i]) src++;
        if (!dout[i]) des++;
    }
    printf("%d\n", src);
    if (scc_cnt == 1) puts("0");
    else printf("%d\n", max(src, des));
    return 0;
}
