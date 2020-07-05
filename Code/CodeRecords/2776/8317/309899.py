#include <cstdio>

using namespace std;

const int P = 10007;

int inv[P], fac[P], ifac[P];

int binom(int n, int m) {
    if (m > n)
        return 0;
    return fac[n] * ifac[m] % P * ifac[n - m] % P;
}

int lucas(int n, int m) {
    if (m > n)
        return 0;
    if (m == 0)
        return 1;
    return binom(n % P, m % P) * lucas(n / P, m / P) % P;
}

int main() {

    inv[1] = 1;
    for (int x = 2; x < P; ++x)
        inv[x] = -(P / x) * inv[P % x] % P + P;
    fac[0] = ifac[0] = 1;
    for (int x = 1; x < P; ++x) {
        fac[x] = fac[x - 1] * x % P;
        ifac[x] = ifac[x - 1] * inv[x] % P;
    }
    int n, m;
    scanf("%d%d", &n, &m);
    printf("%d\n", lucas(n * m, n - 1) * inv[n] % P);

    return 0;
}