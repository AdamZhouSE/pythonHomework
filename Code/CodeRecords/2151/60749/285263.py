#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
const int N = 105, P = 1000000007;

void exgcd(int a, int b, int &x, int &y) {
    if (!b) {
        x = 1;
        y = 0;
        return;
    }
    exgcd(b, a % b, x, y);
    int t = x;
    x = y;
    y = t - a / b * y;
}

int getinv(int a) {
    int x, y;
    exgcd(a, P, x, y);
    return (x + P) % P;
}

const int inv3 = getinv(3);
const int coef = P - 3;
// 扩域 a + b \sqrt{ -3 }
// w[0] = (1, 0)
// w[1] = (-1/2, 1/2)
// w[2] = (-1/2, -1/2)

struct cp {
    int x, y;
    cp(int dx = 0, int dy = 0) : x(dx), y(dy) {}
} w[3], f[N][N], F[3];

cp operator+(const cp &a, const cp &b) { return cp((a.x + b.x) % P, (a.y + b.y) % P); }

cp operator-(const cp &a, const cp &b) { return cp((a.x + P - b.x) % P, (a.y + P - b.y) % P); }

cp operator*(const cp &a, const cp &b) {
    return cp(((ll)a.x * b.x + (ll)a.y * b.y % P * coef) % P, ((ll)a.x * b.y + (ll)a.y * b.x) % P);
}

cp operator*(const cp &a, const int &k) { return cp((ll)a.x * k % P, (ll)a.y * k % P); }

cp operator/(const cp &a, const cp &b) {
    return a * cp(b.x, P - b.y) * getinv((((ll)b.x * b.x - (ll)b.y * b.y % P * coef) % P + P) % P);
}

void operator+=(cp &a, const cp &b) { a = a + b; }
void operator-=(cp &a, const cp &b) { a = a - b; }

cp det(int n) {
    cp res(1, 0);
    int i, j, k, t = 0;
    for (i = 1; i <= n; i++) {
        for (j = i; j <= n; j++)
            if (f[j][i].x || f[j][i].y)
                break;
        if (j > n)
            return cp();
        if (i != j)
            swap(f[i], f[j]), t = !t;
        res = res * f[i][i];
        for (j = i + 1; j <= n; j++) {
            cp p = f[j][i] / f[i][i];
            for (k = i; k <= n; k++) f[j][k] -= f[i][k] * p;
        }
    }
    if (t)
        res = cp() - res;
    return res;
}

int n, m, ans;

struct Edge {
    int u, v, w;
};
vector<Edge> v;

int main() {
    freopen("sum.in", "r", stdin);
    freopen("sum.out", "w", stdout);
    scanf("%d%d", &n, &m);
    v.resize(m);
    for (int i = 0; i < m; i++) scanf("%d%d%d", &v[i].u, &v[i].v, &v[i].w);
    w[0] = cp(1, 0);
    w[1] = cp(P / 2, (P + 1) / 2);
    w[2] = cp(P / 2, P / 2);
    for (int q = 1; q <= 10000; q *= 3) {
        for (int d : { 0, 1, 2 }) {
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++) f[i][j] = cp();
            for (auto &p : v) {
                cp tmp(1, 0);
                for (int j = p.w % 3; j; --j) tmp = tmp * w[d];
                f[p.u][p.u] += tmp;
                f[p.v][p.v] += tmp;
                f[p.u][p.v] -= tmp;
                f[p.v][p.u] -= tmp;
            }
            F[d] = det(n - 1);
        }
        cp f1 = (F[0] + F[1] * w[2] + F[2] * w[1]) * inv3;
        cp f2 = (F[0] + F[1] * w[1] + F[2] * w[2]) * inv3;
        ans = (ans + 1ll * f1.x * q + 2ll * f2.x * q) % P;
        for (auto &p : v) p.w /= 3;
    }
    printf("%d", ans);
    return 0;
}