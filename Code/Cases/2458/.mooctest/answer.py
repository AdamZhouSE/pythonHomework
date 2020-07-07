#include <cstdio>
#include <algorithm>
#define N 1005 
int pos[5][N], p[5][N], n, k, x, f[N];
int main() {
    std::scanf("%d%d", &n, &k);
    for (int i = 0; i < k; i++)
        for (int j = 1; j <= n; j++) std::scanf("%d", &p[i][j]), pos[i][p[i][j]] = j;
    for (int i = 1; i <= n; i++) f[i] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j < i; j++) {
            int v = p[0][i], u = p[0][j];
            int flag = 1;
            for (int t = 1; t < k && flag; t++) if (pos[t][v] < pos[t][u]) flag = 0;
            if (flag) f[v] = std::max(f[v], f[u] + 1);
        }
    int ans = 0;
    for (int i = 1; i <= n; i++) ans = std::max(ans, f[i]);
    std::printf("%d\n", ans); 
    return 0;
}