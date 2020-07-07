#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 105;
int n, m, g[maxn][maxn], match[maxn], used[maxn];
bool find(int x) {
    for (int i = m + 1; i <= n; i++) {
        if (g[x][i] && !used[i]) {
            used[i] = true;
            if (!match[i] || find(match[i])) {
                match[i] = x;
                return true;
            }
        }
    }
    return false;
}
int main() {
    ios::sync_with_stdio(false);
    cin >> n >> m;
    int u, v;
    while (cin >> u >> v) {
        g[u][v] = 1;
    }
    int ans = 0;
    for (int i = 1; i <= m; i++) {
        memset(used, 0, sizeof used);
        if (find(i))
            ans++;
    }
    cout << ans << endl;
    return 0;
}