#include <bits/stdc++.h>

#define ll long long
#define Max 200005

using namespace std;

inline char gc() {
    static char buf[100000], *p1 = buf, *p2 = buf;
    return p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 100000, stdin), p1 == p2) ? EOF : *p1++;
}
#define gc getchar
inline int read() {
    int x = 0;
    char ch = gc();
    bool positive = 1;
    for (; !isdigit(ch); ch = gc())
        if (ch == '-')
            positive = 0;
    for (; isdigit(ch); ch = gc()) x = x * 10 + ch - '0';
    return positive ? x : -x;
}

inline void write(int x) {
    if (x < 0)
        x = -x, putchar('-');
    if (x > 9)
        write(x / 10);
    putchar(x % 10 + '0');
}

inline void writeln(int x) {
    write(x);
    puts("");
}

const int wzp = 1e9 + 7;

struct Edge {
    int v, to;
} e[Max * 2], E[Max * 2];

int t, n, m, l, r, num, cnt, tot, ans, size, rt[Max], dep[Max], deg[Max], dfn[Max], sum[Max], low[Max],
    Deg[Max], head[Max], Head[Max];
bool cut[Max], vis[Max];
char s[Max];
stack<int> stk;

inline int qpow(int x, int y) {
    // cout<<x<<endl;
    int ans = 1;
    while (y) {
        if (y & 1)
            ans = (ll)ans * x % wzp;
        x = (ll)x * x % wzp;
        y >>= 1;
    }
    return ans;
}

inline void add(int u, int v) {
    e[++size].v = v;
    e[size].to = head[u];
    head[u] = size;
}

inline void Add(int u, int v) {
    E[++size].v = v;
    E[size].to = Head[u];
    Head[u] = size;
}

inline void tarjan(int u, int root) {
    // cout<<u<<" "<<root<<endl;
    int son = 0;
    dfn[u] = low[u] = ++cnt;
    for (int i = head[u]; i; i = e[i].to) {
        int v = e[i].v;
        // cout<<u<<" "<<v<<" "<<dfn[v]<<endl;
        if (!dfn[v]) {
            stk.push(i);
            son++;
            tarjan(v, root);
            low[u] = min(low[u], low[v]);
            if (low[v] >= dfn[u]) {
                cut[u] = true;
                tot++;
                Add(u, n + tot);
                Add(n + tot, u);
                Deg[u]++;
                Deg[n + tot]++;
                while (!stk.empty()) {
                    int now = e[stk.top()].v;
                    stk.pop();
                    Add(now, n + tot);
                    Add(n + tot, now);
                    Deg[now]++;
                    Deg[n + tot]++;
                    if (now == v)
                        break;
                }
            }
        } else {
            low[u] = min(low[u], dfn[v]);
        }
    }
    if (u == root) {
        if (son >= 2) {
            cut[u] = true;
        } else {
            cut[u] = false;
        }
    }
    return;
}

inline void dfs(int u, int fa, int root) {
    rt[u] = root;
    vis[u] = true;
    dep[u] = dep[fa] + 1;
    if (u <= n && s[u] != '0')
        sum[u] = 1;
    for (int i = Head[u]; i; i = E[i].to) {
        int v = E[i].v;
        if (vis[v])
            continue;
        dfs(v, u, root);
        sum[u] += sum[v];
    }
    return;
}

int main() {
    // freopen("1.in","r",stdin);
    // freopen("1.out","w",stdout);
    t = read();
    while (t--) {
        size = 0;
        n = read();
        m = read();
        memset(deg, 0, sizeof deg);
        memset(head, 0, sizeof head);
        for (int i = 1; i <= m; i++) {
            l = read();
            r = read();
            add(l, r);
            add(r, l);
            deg[l]++;
            deg[r]++;
        }
        scanf("%s", s + 1);
        num = 0;
        for (int i = 1; i <= n; i++) {
            if (s[i] != '0')
                num++;
        }
        tot = size = 0;
        memset(dfn, 0, sizeof dfn);
        memset(cut, 0, sizeof cut);
        memset(vis, 0, sizeof vis);
        memset(sum, 0, sizeof sum);
        memset(dep, 0, sizeof dep);
        memset(Deg, 0, sizeof Deg);
        memset(Head, 0, sizeof Head);
        for (int i = 1; i <= n; i++) {
            if (!dfn[i]) {
                tarjan(i, i);
            }
        }
        // cout<<"-------------"<<endl;
        // for(int u=1;u<=n+tot;u++){
        //     // cout<<u<<":";
        //     for(int i=Head[u];i;i=E[i].to){
        //         int v=E[i].v;
        //         cout<<v<<" "<<u<<endl;;
        //     }
        //     // cout<<endl;
        // }
        // cout<<"------------"<<endl;
        int o = 0;
        ans = 0;
        for (int i = 1; i <= n; i++) {
            if (!vis[i]) {
                ans++;
                dfs(i, i, i);
                // cout<<i<<" & "<<sum[i]<<endl;
                if (sum[i] & 1)
                    o++;
            }
        }
        // cout<<o<<endl;
        // for(int i=1;i<=n+tot;i++)cout<<sum[i]<<" ";cout<<endl;
        if (o) {
            write(0);
            putchar(' ');
        } else {
            write(qpow(2, m - n + ans));
            putchar(' ');
        }
        for (int i = 1; i <= n; i++) {
            // cout<<i<<endl;
            if (cut[i]) {
                // cout<<"*"<<i<<endl;
                int u = i;
                bool flag = true;
                for (int j = Head[u]; j; j = E[j].to) {
                    int v = E[j].v;
                    // cout<<v<<" & "<<sum[v]<<endl;
                    int now;
                    if (dep[v] < dep[u]) {
                        now = sum[rt[v]] - sum[u];
                    } else {
                        now = sum[v];
                    }
                    if (now & 1) {
                        flag = false;
                        break;
                    }
                }
                if (flag && ((o == 0) || ((o == 1) && (sum[rt[u]] & 1)))) {
                    // cout<<sum[rt[i]]<<" "<<deg[i]<<" "<<Deg[i]<<" "<<((m-deg[i])-(n-1)+Deg[i])<<endl;
                    write(qpow(2, (m - deg[i]) - (n - 1) + Deg[i] - 1 + ans));
                    putchar(' ');
                } else {
                    write(0);
                    putchar(' ');
                }
            } else {
                int now = sum[rt[i]];
                if (s[i] != '0')
                    now--;
                // cout<<i<<" & "<<deg[i]<<" & "<<ans<<endl;
                if ((!(now & 1)) && ((o == 1 && (sum[rt[i]] & 1)) || (o == 0))) {
                    if (!deg[i]) {
                        write(qpow(2, m - n + ans));
                        putchar(' ');
                    } else {
                        write(qpow(2, (m - deg[i]) - (n - 1) + ans));
                        putchar(' ');
                    }
                } else {
                    write(0);
                    putchar(' ');
                }
            }
        }
        puts("");
    }
    return 0;
}