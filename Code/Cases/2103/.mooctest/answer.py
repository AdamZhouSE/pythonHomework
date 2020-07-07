#include <iostream>
#include <cstdio>

using namespace std;

#define MaxN 300005
#define ll long long
#define re register
#define mod 998244353

int n, m;

struct tree {
    int to;
    int next;

} t[MaxN * 2];
int head[MaxN];
int ecnt = 0;
void add(int x, int y) {
    ecnt++;
    t[ecnt].to = y;
    t[ecnt].next = head[x];
    head[x] = ecnt;
}

ll qpow(ll x, ll y) {
    if (x == 0) {
        return 0;
    }
    ll res = 1;
    for (re ll i = y; i; i >>= 1) {
        if (i & 1) {
            res *= x;
            res %= mod;
        }
        x *= x;
        x %= mod;
    }

    return res;
}

ll lg2[MaxN];
ll f[MaxN][55] = { 0 };
ll jup[MaxN][30];
int depth[MaxN];
void dfs(int now, int fat, int dep) {
    jup[now][0] = fat;
    depth[now] = dep;
    for (re int i = 0; i <= 50; ++i) {
        f[now][i] = f[fat][i] + qpow(dep, i);
        f[now][i] %= mod;
    }
    for (re int i = 1; i <= lg2[dep]; ++i) {
        jup[now][i] = jup[jup[now][i - 1]][i - 1];
    }
    for (re int i = head[now]; i != 0; i = t[i].next) {
        int to = t[i].to;
        if (to != fat) {
            dfs(to, now, dep + 1);
        }
    }
}

inline int read() {
    int num = 0, sgn = 1;
    char ch = getchar();
    while (ch != '-' && (ch < '0' || ch > '9')) {
        ch = getchar();
    }
    if (ch == '-') {
        sgn = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        num *= 10;
        num += ch - '0';
        ch = getchar();
    }
    return num * sgn;
}

int main() {
    // scanf("%d",&n);
    n = read();
    for (re int i = 1; i < n; ++i) {
        int x, y;
        // scanf("%d%d",&x,&y);
        x = read();
        y = read();
        add(x, y);
        add(y, x);
    }
    for (re int i = 1; i <= n; ++i) {
        lg2[i] = lg2[i - 1] + ((1 << (lg2[i - 1] + 1)) == i);
    }
    //	for(re int i=1;i<=n;++i)
    //	{
    //		cout<<lg2[i]<<" ";
    //	}

    dfs(1, 0, 0);

    // scanf("%d",&m);
    m = read();
    for (re int it = 1; it <= m; ++it) {
        int lef, rit, k, lca;
        // scanf("%d%d%d",&lef,&rit,&k);
        lef = read();
        rit = read();
        k = read();
        // if(k == 0) {printf("0\n");continue;}
        if (depth[lef] < depth[rit]) {
            swap(lef, rit);
        }

        ll jl = lef, jr = rit;
        while (depth[jl] > depth[jr]) {
            jl = jup[jl][lg2[depth[jl] - depth[jr]]];
        }
        // cout<<jl<<" "<<jr<<" "<<depth[jl]<<" "<<depth[jr]<<endl;
        if (jl == jr) {
            lca = jr;
        } else {
            for (re int i = lg2[depth[rit]]; i >= 0; --i) {
                if (jup[jl][i] != jup[jr][i]) {
                    jl = jup[jl][i];
                    jr = jup[jr][i];
                }
            }

            lca = jup[jr][0];
        }
        //		cout<<lca<<endl;
        //		cout<<f[lef][k]<<" "<<f[rit][k]<<" "<<2*f[lca][k]<<" "<<qpow(depth[lca],k)<<endl;
        ll ans = f[lef][k] + f[rit][k] - 2 * f[lca][k] + qpow(depth[lca], k) + (ll)mod * 10;
        ans %= mod;
        printf("%lld\n", ans);
    }

    return 0;
}