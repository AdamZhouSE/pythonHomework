#include <bits/stdc++.h>

template <class T>
inline void read(T &x) {
    static char ch;
    while (!isdigit(ch = getchar()))
        ;
    x = ch - '0';
    while (isdigit(ch = getchar())) x = x * 10 + ch - '0';
}

template <class T>
inline void relax(T &x, const T &y) {
    if (x < y)
        x = y;
}

const int MaxN = 1e2 + 5;
const int MaxM = 1e4 + 5;

const int mod = 1e9 + 7;
const int sqrt3 = 82062379;
const int inv2 = (mod + 1) / 2;
const int inv3 = (mod + 1) / 3;

inline int qpow(int x, int y) {
    int res = 1;
    for (; y; y >>= 1, x = 1LL * x * x % mod)
        if (y & 1)
            res = 1LL * res * x % mod;
    return res;
}

inline void add(int &x, const int &y) {
    x += y;
    if (x >= mod)
        x -= mod;
}

inline void dec(int &x, const int &y) {
    x -= y;
    if (x < 0)
        x += mod;
}

struct edge {
    int u, v, w;
    inline void scan() { read(u), read(v), read(w); }
} e[MaxM];

struct complex {
    int x, y;
    complex() {}
    complex(int _x, int _y) : x(_x), y(_y) {}
    inline bool has() const { return x || y; }
    inline complex operator+(const complex &rhs) const {
        complex res(x, y);
        add(res.x, rhs.x), add(res.y, rhs.y);
        return res;
    }
    inline complex operator-(const complex &rhs) const {
        complex res(x, y);
        dec(res.x, rhs.x), dec(res.y, rhs.y);
        return res;
    }
    inline complex operator*(const complex &rhs) const {
        int a = (1LL * x * rhs.x - 1LL * y * rhs.y) % mod;
        int b = (1LL * x * rhs.y + 1LL * y * rhs.x) % mod;
        return complex(a < 0 ? a + mod : a, b);
    }
    inline complex inv() const {
        int norm_inv = qpow((1LL * x * x + 1LL * y * y) % mod, mod - 2);
        return complex(1LL * x * norm_inv % mod, 1LL * (mod - y) * norm_inv % mod);
    }
    inline complex neg() const { return complex(x ? mod - x : 0, y ? mod - y : 0); }
} omega[3];

int n, m;
int maxw;
complex mat[MaxN][MaxN];

inline complex det(int n) {
    complex res(1, 0);
    for (int i = 1; i <= n; ++i) {
        int p = 0;
        for (int j = i; j <= n; ++j)
            if (mat[j][i].has()) {
                p = j;
                break;
            }
        if (!p)
            return complex(0, 0);
        else if (p != i) {
            res = res.neg();
            for (int j = i; j <= n; ++j) std::swap(mat[p][j], mat[i][j]);
        }
        res = res * mat[i][i];

        complex inv = mat[i][i].inv();
        for (int j = i + 1; j <= n; ++j)
            if (mat[j][i].has()) {
                complex t = mat[j][i] * inv;
                for (int k = i; k <= n; ++k) mat[j][k] = mat[j][k] - mat[i][k] * t;
            }
    }
    return res;
}

int main() {
    freopen("sum.in", "r", stdin);
    freopen("sum.out", "w", stdout);

    read(n), read(m);
    for (int i = 1; i <= m; ++i) {
        e[i].scan();
        relax(maxw, e[i].w);
    }

    omega[0] = complex(1, 0);
    omega[1] = complex(mod - inv2, 1LL * inv2 * sqrt3 % mod);
    omega[2] = omega[1] * omega[1];

    int ans = 0;
    for (int p = 1; p <= maxw; p *= 3) {
        static int weight[MaxM];
        static complex a[3], b[3];
        for (int i = 1; i <= m; ++i) weight[i] = (e[i].w / p) % 3;

        for (int t = 0; t < 3; ++t) {
            memset(mat, 0, sizeof(mat));

            static complex pw[3];
            for (int i = 0; i < 3; ++i) pw[i] = omega[i * t % 3];
            for (int i = 1; i <= m; ++i) {
                int u = e[i].u, v = e[i].v;
                complex w = pw[weight[i]];

                mat[u][u] = mat[u][u] + w;
                mat[v][v] = mat[v][v] + w;
                mat[u][v] = mat[u][v] - w;
                mat[v][u] = mat[v][u] - w;
            }
            a[t] = det(n - 1);
        }

        b[1] = a[0] + a[1] * omega[2] + a[2] * omega[1];
        b[2] = a[0] + a[1] * omega[1] + a[2] * omega[2];

        //	std::cout << b[1].y << ' ' << b[2].y << '\n';
        //	assert(b[1].y == 0 && b[2].y == 0);
        ans = ((b[1].x + b[2].x * 2LL) * p + ans) % mod;
    }

    ans = 1LL * ans * inv3 % mod;
    std::cout << ans << std::endl;

    return 0;
}