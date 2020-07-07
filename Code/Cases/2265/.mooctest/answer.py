#include <bits/stdc++.h>
using namespace std;
const int maxn = 105;
int n;
struct edge {
    int u, v, nxt;
} e[maxn * maxn];
int head[maxn], js;
void addage(int u, int v) {
    e[++js].u = u;
    e[js].v = v;
    e[js].nxt = head[u];
    head[u] = js;
}
int low[maxn], dfn[maxn], cnt, st[maxn], top, lts;
bool cut[maxn];
vector<int> lt[maxn];
void tarjan(int u, int rt) {
    low[u] = dfn[u] = ++cnt;
    st[++top] = u;
    int ct = 0;
    for (int i = head[u]; i; i = e[i].nxt) {
        int v = e[i].v;
        if (!dfn[v]) {
            ct++;
            tarjan(v, rt);
            low[u] = min(low[u], low[v]);
            if ((ct > 1 && u == rt) || (u != rt && low[v] >= dfn[u]))
                cut[u] = 1;
            /*
                        if(low[v]>=dfn[u])
                        {
                            lts++;
                            lt[lts].clear();
                            while(st[top]!=u)lt[lts].push_back(st[top--]);
                            lt[lts].push_back(u);
                        }
            */
        } else
            low[u] = min(low[u], dfn[v]);
    }
}
void init() {
    memset(head, 0, sizeof head);
    js = 0;
    memset(low, 0, sizeof low);
    memset(dfn, 0, sizeof dfn);
    cnt = 0;
    top = 0;
    lts = 0;
    memset(cut, 0, sizeof cut);
}
int main() {
    while (scanf("%d", &n), n) {
        init();
        int u, v;
        while (scanf("%d", &u), u) {
            while (1) {
                scanf("%d", &v);
                addage(u, v);
                addage(v, u);
                char c = getchar();
                if (c == '\n')
                    break;
            }
        }
        for (int i = 1; i <= n; ++i)
            if (!dfn[i])
                tarjan(i, i);
        int jss = 0;
        for (int i = 1; i <= n; ++i)
            if (cut[i])
                jss++;
        printf("%d\n", jss);
    }
    return 0;
}