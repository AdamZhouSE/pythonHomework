#include <bits/stdc++.h>
using namespace std;

bool A_1;
inline int read_() {
    int x_ = 0, f_ = 1;
    char c_ = getchar();
    while (c_ < '0' || c_ > '9') {
        if (c_ == '-')
            f_ = -1;
        c_ = getchar();
    }
    while (c_ >= '0' && c_ <= '9') {
        x_ = (x_ << 1) + (x_ << 3) + c_ - '0';
        c_ = getchar();
    }
    return x_ * f_;
}

#define maxn 22
#define maxq 12
#define maxm 59050
#define INF 0x3f3f3f3f
int bit[maxq], a[maxq], n, m, q, d[maxn][maxn], s[maxq], t[maxq], l[maxq], r[maxq], f[maxm][maxn];
bool A_2;

inline void get_(int x) {
    int cnt = 0;
    memset(a, 0, sizeof(a));
    while (x) {
        a[cnt++] = x % 3;
        x /= 3;
    }
}

inline int sum_() {
    int ans = 0;
    for (int i = 0; i < q; ++i) {
        ans += a[i] * bit[i];
    }
    return ans;
}

int main() {
    //	printf("%lf",(double) ( &A_2 - &A_1 ) / ( 1 << 20 ) );
    //	freopen("a.txt","r",stdin);
    memset(d, 0x3f, sizeof(d));
    n = read_();
    m = read_();
    q = read_();
    int x, y, z;
    for (int i = 1; i <= m; ++i) {
        x = read_();
        y = read_();
        z = read_();
        --x, --y;
        d[x][y] = min(d[x][y], z);
    }
    for (int i = 0; i < n; ++i) d[i][i] = 0;
    for (int i = 0; i < q; ++i) {
        s[i] = read_(), --s[i];
        t[i] = read_(), --t[i];
        l[i] = read_();
        r[i] = read_();
    }
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (d[i][k] == INF)
                continue;
            for (int j = 0; j < n; ++j) {
                if (d[k][j] == INF)
                    continue;
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    bit[0] = 1;
    for (int i = 1; i <= q; ++i) bit[i] = bit[i - 1] * 3;
    memset(f, 0x3f, sizeof(f));
    f[0][0] = 0;
    int ans = 0;
    for (int S = 0; S < bit[q]; ++S) {
        get_(S);
        for (int i = 0; i < n; ++i) {
            if (f[S][i] == INF)
                continue;
            for (int j = 0; j < q; ++j) {
                if (a[j] == 0) {
                    ++a[j];
                    int v = sum_();
                    f[v][s[j]] = min(f[v][s[j]], max(f[S][i] + d[i][s[j]], l[j]));
                    --a[j];
                } else if (a[j] == 1) {
                    if (f[S][i] + d[i][t[j]] <= r[j]) {
                        ++a[j];
                        int v = sum_();
                        f[v][t[j]] = min(f[v][t[j]], f[S][i] + d[i][t[j]]);
                        --a[j];
                    }
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            if (f[S][i] == INF)
                continue;
            int cnt = 0;
            for (int j = 0; j < q; ++j)
                if (a[j] == 2)
                    ++cnt;
            ans = max(ans, cnt);
        }
    }

    printf("%d", ans);
    return 0;
}