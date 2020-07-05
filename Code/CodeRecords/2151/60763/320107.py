#include <bits/stdc++.h>
#define mod 1000000007
#define inv3 333333336
#define inv2 500000004
#define rt3 82062379
using namespace std;
int add(int a, int b) {
    a += b;
    return a >= mod ? a - mod : a;
}
int sub(int a, int b) { return add(a, mod - b); }
int ksm(int a, int b) {
    int s = 1;
    for (; b; b >>= 1, a = 1ll * a * a % mod)
        if (b & 1)
            s = 1ll * s * a % mod;
    return s;
}
struct Complex {
    int a, b;
    inline Complex(int _a = 0, int _b = 0) { a = _a, b = _b; }

    inline Complex operator+(Complex y) const { return Complex(add(a, y.a), add(b, y.b)); }

    inline Complex operator-(Complex y) const { return Complex(sub(a, y.a), sub(b, y.b)); }

    inline Complex operator*(Complex y) const {
        return Complex(sub(1ll * a * y.a % mod, 1ll * b * y.b % mod),
                       add(1ll * a * y.b % mod, 1ll * b * y.a % mod));
    }

    inline Complex operator*(int y) const { return Complex(1ll * a * y % mod, 1ll * b * y % mod); }

    inline Complex operator/(int y) const {
        int inv = ksm(y, mod - 2);
        return Complex(1ll * a * inv % mod, 1ll * b * inv % mod);
    }

    inline Complex operator/(Complex y) const {
        return Complex(a, b) * Complex(y.a, mod - y.b) / add(1ll * y.a * y.a % mod, 1ll * y.b * y.b % mod);
    }
} a[105][105], w[3], invw[3];
Complex Det(int n) {
    Complex ret = Complex(1, 0);
    for (int i = 1; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (a[j][i].a || a[j][i].b) {
                if (i == j)
                    break;
                swap(a[i], a[j]), ret = ret * (mod - 1);
                break;
            }
        }
        for (int j = i + 1; j < n; j++) {
            Complex inv = a[j][i] / a[i][i];
            for (int k = i; k < n; k++) a[j][k] = a[j][k] - inv * a[i][k];
        }
        ret = ret * a[i][i];
    }
    return ret;
}
inline void IDFT(Complex *p)  //我抄的
{
    Complex tmp[3];
    tmp[0] = p[0], tmp[1] = p[1], tmp[2] = p[2];
    p[0] = tmp[0] + tmp[1] + tmp[2];
    p[1] = tmp[0] + tmp[1] * invw[1] + tmp[2] * invw[2];
    p[2] = tmp[0] + tmp[1] * invw[2] + tmp[2] * invw[1];
    for (int i = 0; i < 3; ++i) p[i] = p[i] * inv3;
}
void GetW()  //也是抄的
{
    w[0] = Complex(1, 0), w[1] = Complex(mod - inv2, 1ll * rt3 * inv2 % mod);
    w[2] = Complex(mod - inv2, mod - 1ll * rt3 * inv2 % mod);
    invw[0] = Complex(1, 0) / w[0], invw[1] = Complex(1, 0) / w[1], invw[2] = Complex(1, 0) / w[2];
}
int n, m, u[10005], v[10005], val[10005], ans;
int main() {
    freopen("sum.in", "r", stdin);
    freopen("sum.out", "w", stdout);
    GetW();
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= m; i++) scanf("%d%d%d", &u[i], &v[i], &val[i]);
    for (int i = 0, pw = 1; i <= 9; i++, pw = 3ll * pw % mod) {
        Complex res[3];
        for (int j = 0; j < 3; j++) {
            Complex w0 = Complex(1, 0), w1 = w[j], w2 = w[(j + j) % 3];
            memset(a, 0, sizeof(a));
            for (int k = 1; k <= m; k++) {
                int ty = val[k] % 3;
                Complex now = (ty == 0 ? w0 : (ty == 1 ? w1 : w2));
                a[u[k]][u[k]] = a[u[k]][u[k]] + now;
                a[v[k]][v[k]] = a[v[k]][v[k]] + now;
                a[u[k]][v[k]] = a[u[k]][v[k]] - now;
                a[v[k]][u[k]] = a[v[k]][u[k]] - now;
            }
            res[j] = Det(n);
        }
        IDFT(res);
        ans = add(ans, add(1ll * pw * res[1].a % mod, 2ll * pw * res[2].a % mod));
        for (int j = 1; j <= m; j++) val[j] /= 3;
    }
    printf("%d\n", ans);
}