#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int read() {
    int ans = 0, flag = 1;
    char ch = getchar();
    while(ch < '0' || ch > '9') {if(ch == '-') flag = - flag; ch = getchar();}
    while(ch >= '0' && ch <= '9') {ans = ans * 10 + ch - '0'; ch = getchar();}
    return ans * flag;
}
const int N = 100010;
const int mod = 1000000007;
struct Graph {
    int deg[N << 1];
    int f[N << 2], t[N << 2], n[N << 2], head[N << 1], tot;
    void addedge(int u, int v) {
        ++ tot; ++ deg[u]; ++ deg[v];
        f[tot] = u;
        t[tot] = v;
        n[tot] = head[u];
        head[u] = tot;
    }
}G, H;
int low[N], dfn[N], DFN;
int sta[N << 2], top;
int bel[N], cnt;
int n, m;

int col[N];
char s[N];
int beg[N], bcnt;//the beg's top Node and the num of beg

int ansBeg[N];//the ans of the beg if not del ant Node
int belBeg[N];//which beg is the Node belong to;
int nodBeg[N];//howmany Node in the beg
int edgBeg[N];//howmany Edge in the beg
int colBeg[N];//how many black Node in the beg

int Ans[N];
int colSum[N << 1];
int bin[N];
void clear() {
    memset(&G, 0, sizeof(G));
    memset(&H, 0, sizeof(H));
    memset(low, 0, sizeof(low));
    memset(dfn, 0, sizeof(dfn));
    memset(sta, 0, sizeof(sta));
    memset(bel, 0, sizeof(bel));
    DFN = top = cnt = 0;

    memset(col, 0, sizeof(col));
    memset(belBeg, 0, sizeof(belBeg));
    while(bcnt) {
        beg[bcnt] = 
        ansBeg[bcnt] = 
        nodBeg[bcnt] = 
        edgBeg[bcnt] =
        colBeg[bcnt] = 0;
        -- bcnt;
    }
    memset(Ans, 0, sizeof(Ans));
    memset(colSum, 0, sizeof(colSum));
}
void dfs1(int x, int bcnt) {
    belBeg[x] = bcnt;
    nodBeg[bcnt] += 1;
    edgBeg[bcnt] += G.deg[x];
    colBeg[bcnt] += col[x];

    low[x] = dfn[x] = ++ DFN;
    for(int i = G.head[x]; i; i = G.n[i]) {
        int t = G.t[i];
        if(!dfn[t]) {
            sta[++ top] = i;
            dfs1(t, bcnt);
            low[x] = min(low[x], low[t]);
            if(low[t] == dfn[x]) {
                ++ cnt;
                H.addedge(x, n + cnt);
                H.addedge(n + cnt, x);
                bel[x] = cnt;
                H.addedge(t, n + cnt);
                H.addedge(n + cnt, t);
                bel[t] = cnt;
                for(; sta[top] != i; sta[top --] = 0) {
                    int fr = G.f[sta[top]];
                    int to = G.t[sta[top]];
                    if(bel[fr] != cnt) {
                        H.addedge(fr, n + cnt);
                        H.addedge(n + cnt, fr);
                        bel[fr] = cnt;
                    }
                    if(bel[to] != cnt) {
                        H.addedge(to, n + cnt); 
                        H.addedge(n + cnt, to);
                        bel[to] = cnt;
                    }
                }
                sta[top --] = 0;
            }
        }
        else if(dfn[t] < dfn[x]) {
            sta[++ top] = i;
            low[x] = min(low[x], dfn[t]);
        }
    }
}
void dfs2(int x, int f, int bcnt) {
    if(x <= n) colSum[x] = col[x];
    for(int i = H.head[x]; i; i = H.n[i]) {
        int t = H.t[i];
        if(t == f) continue;
        dfs2(t, x, bcnt);
        colSum[x] += colSum[t];
    }
    if(x > n) return;
    Ans[x] = 1;
    for(int i = H.head[x]; i; i = H.n[i]) {
        int t = H.t[i];
        if(t == f) {
            if((colBeg[bcnt] - colSum[x]) % 2)
                Ans[x] = 0;
        }
        else
            if(colSum[t] % 2)
                Ans[x] = 0;
    }
    Ans[x] = Ans[x] * bin[(edgBeg[bcnt] - G.deg[x]) - max(0, nodBeg[bcnt] - 1 - H.deg[x])];
}
void work() {
    clear();
    n = read(); m = read();
    for(int i = 1; i <= m; ++ i) {
        int u = read(), v = read();
        G.addedge(u, v);
        G.addedge(v, u);
    }
    for(int i = 1; i <= n; ++ i)
        G.deg[i] /= 2;
    scanf("%s", s);
    for(int i = 0; i < n; ++ i)
        col[i + 1] = (s[i] == '1');
    for(int i = 1; i <= n; ++ i)
        if(!dfn[i]) {
            belBeg[i] = ++ bcnt;
            beg[bcnt] = i;
            dfs1(i, bcnt);
        }
    for(int i = 1; i <= n + cnt; ++ i)
        H.deg[i] /= 2;
    for(int i = 1; i <= bcnt; ++ i)
        edgBeg[i] /= 2;
    int ans = 1, Boom = 0;
    for(int i = 1; i <= bcnt; ++ i) {
        if(colBeg[i] % 2) ansBeg[i] = 1;
        else ansBeg[i] = 0;
        Boom += ansBeg[i];
    }
    if(Boom) printf("0 ");
    else printf("%d ", bin[m - n + bcnt]);
    for(int i = 1; i <= bcnt; ++ i)
        dfs2(beg[i], 0, i);
    for(int i = 1; i <= n; ++ i) {
        if(Boom - ansBeg[belBeg[i]]) printf("0 ");
        else printf("%d ", 1ll * Ans[i] * bin[(m - edgBeg[belBeg[i]]) - (n - nodBeg[belBeg[i]]) + (bcnt - 1)] % mod);
    }
    puts("");
}
int main() {
    bin[0] = 1;
    for(int i = 1; i < N; ++ i)
        bin[i] = 1ll * bin[i - 1] * 2 % mod;
    int t = read();
    while(t --)
        work();
    return 0;
}