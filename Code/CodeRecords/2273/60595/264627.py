#include <stdio.h> 
#define inf 999999999
#define setdp(i, j, x) dp[i * (k + 1) + j] = x
#define getdp(i, j) dp[(i) * (k + 1) + j]
#define getod(i, j) ld[(i) * (k + 1) + j] 
/*苹果树放弃了，做不出来了*/
int fr[40010],ne[40010],v[40010],bs = 0,sl[40010],sz[40010],n,k;
void addb(int a, int b) {
    v[bs] = b;
    ne[bs] = fr[a];
    fr[a] = bs++;
}
int xl[40010],si[40010],jl[40010],tm = 0,x1[40010],x2[40010];
void dfs1(int u) {
    x1[u] = tm;
    xl[tm++] = u;
    si[u] = 1;
    for (int i = fr[u]; i != -1; i = ne[i]) {
        jl[v[i]] = jl[u] + sz[v[i]];
        dfs1(v[i]);
        si[u] += si[v[i]];
    }
}
void dfs2(int u) {
    for (int i = fr[u]; i != -1; i = ne[i]) dfs2(v[i]);
    xl[++tm] = u;
    x2[u] = tm;
}
int dl[500010],dz[500010],he = 0,ta = 0,dp[60000010],ld[60000010];
void insert(int i, int x) {
    dz[i] = x;
    while (he < ta && dz[dl[ta - 1]] <= x) ta -= 1;
    dl[ta++] = i;
}
void del(int i) {
    if (he < ta && dl[he] == i) he += 1;
}
int getma() {
    if (he < ta) return dz[dl[he]];
    else return - inf;
}
bool ez[20010],kz[20010];
int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &k);
        bs = 0;
        for (int i = 1; i <= n + n; i++) fr[i] = -1;
        for (int i = 1; i <= n; i++) ez[i] = kz[i] = false;
        for (int i = 1; i <= n; i++) {
            int a;
            scanf("%d%d%d", &a, &sl[i], &sz[i]);
            if (i > 1) addb(a, i);
            ez[a] = true;
        }
        for (int i = 1; i <= n; i++) {
            if (sl[i] > 1) {
                sl[i + n] = sl[i] - 1;
                sz[i + n] = sz[i];
                addb(i, i + n);
                sl[i] = 1;
                kz[i] = true;
            }
        }
        jl[1] = sz[1];
        tm = 0;
        dfs1(1);
        for (int i = tm - 1; i >= 0; i--) {
            he = ta = 0;
            for (int j = 0; j <= k; j++) {
                int u = xl[i],
                ma = getdp(i + si[u], j);
                del(j - sl[u] - 1);
                if (j > 0) insert(j - 1, getdp(i + 1, j - 1) - sz[u] * (j - 1));
                int t = getma() + sz[u] * j;
                if (t > ma) ma = t;
                setdp(i, j, ma);
            }
        }
        for (int i = 0; i <= tm * (k + 1) + k; i++) {
            ld[i] = dp[i];
            dp[i] = 0;
        }
        tm = 0;
        dfs2(1);
        for (int i = 1; i <= tm; i++) {
            he = ta = 0;
            for (int j = 0; j <= k; j++) {
                int u = xl[i],
                ma = getdp(i - si[u], j);
                del(j - sl[u] - 1);
                if (j > 0) insert(j - 1, getdp(i - 1, j - 1) - sz[u] * (j - 1));
                int t = getma() + sz[u] * j;
                if (t > ma) ma = t;
                setdp(i, j, ma);
            }
        }
        int jg = -inf;
        for (int i = 1; i <= n; i++) {
            if (ez[i]) continue;
            int ma = -inf;
            for (int j = 0; j <= k; j++) {
                int t = getod(x1[i] + 1, j);
                if (!kz[i]) t += getdp(x2[i] - 1, k - j);
                else t += getdp(x2[i + n] - 1, k - j);
                if (t > ma) ma = t;
            }
            ma += jl[i];
            if (ma > jg) jg = ma;
        }
        printf("%d\n", jg);
        for (int i = 0; i <= tm * (k + 1) + k; i++) ld[i] = dp[i] = 0;
    }
    return 0;
}