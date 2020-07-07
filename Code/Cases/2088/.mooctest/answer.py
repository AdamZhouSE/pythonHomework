#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 105, P = 1e9 + 7;
int a[N][N], v, ans, n, m, b[N][N], c[N][N];
void gauss(int n) {
    int ans = 1;
    for (int i = 1; i < n; i++) {
        for (int j = i + 1; j < n; j++)
            while (a[j][i]) {
                int t = a[i][i] / a[j][i];
                for (int k = i; k < n; k++) a[i][k] = (a[i][k] - a[j][k] * t) % P;
                swap(a[i], a[j]);
                v = P - v;
            }
        v = (v * a[i][i]) % P;
        if (!v) {
            v = 0;
            return;
        }
    }
}
signed main() {
    scanf("%lld", &n);
    for (int i = 0; i < n - 1; i++) {
        scanf("%lld", &b[i][0]);
        for (int j = 1; j <= b[i][0]; j++) scanf("%lld%lld", &b[i][j], &c[i][j]);
    }
    for (int k = 0; k < (1 << n - 1); k++) {
        int cnt = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) a[i][j] = 0;
        v = 1;
        for (int j = 0; j < n - 1; j++)
            if ((1 << j) & k) {
                cnt++;
                for (int i = 1; i <= b[j][0]; i++) {
                    a[b[j][i]][b[j][i]]++;
                    a[c[j][i]][c[j][i]]++;
                    a[b[j][i]][c[j][i]]--;
                    a[c[j][i]][b[j][i]]--;
                }
            }
        for (int i = 1; i < n; i++)
            for (int j = 1; j < n; j++)
                if (a[i][j] < 0)
                    a[i][j] += P;
        gauss(n);
        if ((n - cnt) & 1)
            (ans += v) %= P;
        else
            (ans += P - v) %= P;
    }
    printf("%lld\n", (ans % P + P) % P);
}