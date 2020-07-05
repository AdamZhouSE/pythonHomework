#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;
const int N = 20000, rt3 = 82062379, mod = 1e9 + 7, inv2 = (mod + 1) / 2, inv3 = (mod + 1) / 3;
int n, m;
inline int read() {
    register int x = 0;
    register char c = getchar();
    while (c < '0' || c > '9') c = getchar();
    while (c >= '0' && c <= '9') x = (((x << 2) + x) << 1) + (c ^ 48), c = getchar();
    return x;
}

int ksm(int a, int k) {
    int ans = 1;
    a %= mod;
    for (; k; k >>= 1, a = (long long)a * a % mod)
        if (k & 1)
            ans = (long long)ans * a % mod;
    return ans;
}

struct node {
    long long a, b;
    node(long long a = 0, long long b = 0) : a(a), b(b) {}
    friend node operator+(const node &A, const node &B) { return node((A.a + B.a) % mod, (A.b + B.b) % mod); }
    friend node operator-(const node &A, const node &B) {
        return node((A.a - B.a + mod) % mod, (A.b - B.b + mod) % mod);
    }
    friend node operator*(const node &A, const node &B) {
        return node((A.a * B.a % mod - A.b * B.b % mod + mod) % mod,
                    (long long)A.a * B.b % mod + (long long)A.b * B.a % mod);
    }
    friend node operator*(const node &A, const int &B) {
        return node(1LL * A.a * B % mod, 1LL * A.b * B % mod);
    }
    friend node operator/(const node &A, const int &B) {
        int inv = ksm(B, mod - 2);
        return A * inv;
    }
    friend node operator/(const node &A, const node &B) {
        return A * node(B.a, mod - B.b) / (1LL * B.a * B.a % mod + 1LL * B.b * B.b % mod);
    }
} w[3], winv[3], a[102][102], coef[3];

int eu[N], ev[N], ec[N], bin[20];

node Det() {
    node res = node(1, 0);
    for (int j = 1; j < n; ++j) {
        for (int i = j; i < n; ++i)
            if (a[i][j].a || a[i][j].b) {
                if (i == j)
                    break;
                swap(a[j], a[i]);
                res = res * (mod - 1);
                break;
            }
        for (int i = j + 1; i < n; ++i) {
            node inv = a[i][j] / a[j][j];
            for (int k = j; k < n; ++k) a[i][k] = a[i][k] - inv * a[j][k];
        }
        res = res * a[j][j];
    }
    return res;
}

inline void IDFT(node *p) {
    int i;
    node tmp[3];
    tmp[0] = p[0], tmp[1] = p[1], tmp[2] = p[2];
    p[0] = tmp[0] + tmp[1] + tmp[2];
    p[1] = tmp[0] + tmp[1] * winv[1] + tmp[2] * winv[2];
    p[2] = tmp[0] + tmp[1] * winv[2] + tmp[2] * winv[1];
    for (i = 0; i < 3; ++i) p[i] = p[i] * inv3;
}

int calc(int p) {
    node w0, w1, w2, c;
    for (int i = 0; i < 3; ++i) {
        memset(a, 0, sizeof a);
        w0 = node(1, 0);
        w1 = w[i];
        w2 = w[(i + i) % 3];
        for (int j = 1; j <= m; ++j) {
            int k = ec[j] / bin[p] % 3;
            c = (k == 1 ? w1 : (k == 2 ? w2 : w0));
            a[eu[j]][eu[j]] = a[eu[j]][eu[j]] + c;
            a[ev[j]][ev[j]] = a[ev[j]][ev[j]] + c;
            a[eu[j]][ev[j]] = a[eu[j]][ev[j]] - c;
            a[ev[j]][eu[j]] = a[ev[j]][eu[j]] - c;
        }
        coef[i] = Det();
    }
    IDFT(coef);
    return ((long long)coef[1].a + (coef[2].a + coef[2].a)) * bin[p] % mod;
}

int main() {
    freopen("sum.in", "r", stdin);
    freopen("sum.out", "w", stdout);
    n = read();
    m = read();
    for (int i = 1; i <= m; ++i) eu[i] = read(), ev[i] = read(), ec[i] = read();
    w[0] = node(1, 0);
    w[1] = node(mod - inv2, 1LL * rt3 * inv2 % mod);
    w[2] = node(mod - inv2, mod - (long long)rt3 * inv2 % mod);
    winv[0] = node(1, 0) / w[0];
    winv[1] = node(1, 0) / w[1];
    winv[2] = node(1, 0) / w[2];
    bin[0] = 1;
    for (int i = 1; i <= 10; ++i) bin[i] = bin[i - 1] * 3;
    int ans = 0;
    for (int i = 0; i <= 10; ++i) ans = ((long long)ans + calc(i)) % mod;
    cout << ans << endl;
    return 0;
}
/*
5 7
3 2 7400
4 1 1618
4 2 9110
4 3 4264
5 1 537
5 2 4240
5 3 655
*/