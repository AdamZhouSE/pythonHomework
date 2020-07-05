#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define inf 0x3f3f3f3f
#define LL_inf (1ll << 60)
const int maxn = 20 + 5;
const int mod = 1e9 + 7;
int n, m, q;
int dis[maxn][maxn];
struct node {
    int s, t, l, r;
} sto[15];
void floyed() {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k]);
            }
        }
    }
}
int third[maxn];
int dp[maxn][60005];
void solve(int maxstate) {
    memset(dp, inf, sizeof(dp));
    dp[1][0] = 0;
    for (int i = 0; i <= maxstate; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= q; k++) {
                int tmp = i % third[k + 1] / third[k];
                if (tmp == 0 && dp[j][i] + dis[j][sto[k].s] <= sto[k].r) {
                    dp[sto[k].s][i + third[k]] =
                        min(dp[sto[k].s][i + third[k]], max(sto[k].l, dp[j][i] + dis[j][sto[k].s]));// 注意这里应该取最大值，有可能到了还没到规定的取货时间
                }
                if (tmp == 1 && dp[j][i] + dis[j][sto[k].t] <= sto[k].r) {
                    dp[sto[k].t][i + third[k]] = min(dp[sto[k].t][i + third[k]], dp[j][i] + dis[j][sto[k].t]);
                }
            }
        }
    }
}
int main() {
    scanf("%d %d %d", &n, &m, &q);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j)
                dis[i][j] = 0;
            else
                dis[i][j] = inf;
        }
    }
    int st, ed, val;
    while (m--) {
        scanf("%d %d %d", &st, &ed, &val);
        dis[st][ed] = min(dis[st][ed], val);
    }
    for (int i = 1; i <= q; i++) {
        scanf("%d %d %d %d", &sto[i].s, &sto[i].t, &sto[i].l, &sto[i].r);
    }
    floyed();
    third[1] = 1;
    for (int i = 2; i <= q + 1; i++) {
        third[i] = third[i - 1] * 3;
    }
    solve(third[q + 1] - 1);
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= third[q + 1] - 1; j++) {
            if (dp[i][j] >= inf)
                continue;
            int tmp = 0;
            for (int k = 1; k <= q; k++) {
                tmp += ((j % third[k + 1] / third[k]) == 2 ? 1 : 0);
            }
            ans = max(ans, tmp);
        }
    }
    printf("%d\n", ans);
    return 0;
}