#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define ll long long
#define gc getchar()
using namespace std;
const int N = 1e6 + 10;
int sa[N], wa[N], wb[N], c[N], wv[N];
char s[N];
bool cmp(int *r, int a, int b, int l) { return r[a] == r[b] && r[a + l] == r[b + l]; }
void DA(char *r, int n, int m) {
    int *x = wa, *y = wb, *t;
    for (int i = 1; i <= n; i++) ++c[x[i] = r[i]];
    for (int i = 2; i <= m; i++) c[i] += c[i - 1];
    for (int i = n; i >= 1; i--) sa[c[x[i]]--] = i;
    for (int j = 1, p; p < n; j <<= 1, m = p) {
        p = 0;
        for (int i = n - j + 1; i <= n; i++) y[++p] = i;
        for (int i = 1; i <= n; i++)
            if (sa[i] > j)
                y[++p] = sa[i] - j;

        for (int i = 1; i <= m; i++) c[i] = 0;
        for (int i = 1; i <= n; i++) ++c[wv[i] = x[y[i]]];
        for (int i = 2; i <= m; i++) c[i] += c[i - 1];
        for (int i = n; i >= 1; i--) sa[c[wv[i]]--] = y[i];
        t = x;
        x = y;
        y = t;
        p = 1;
        x[sa[1]] = 1;
        for (int i = 2; i <= n; i++) x[sa[i]] = cmp(y, sa[i], sa[i - 1], j) ? p : ++p;
    }
    for (int i = 1; i <= n; i++) printf("%d ", sa[i]);
}
int main() {
    scanf("%s", s + 1);
    int n = strlen(s + 1), m = 122;
    DA(s, n, m);
    return 0;
}