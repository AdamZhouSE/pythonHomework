#include<bits/stdc++.h>
using namespace std;

#define N 100001
#define rep(i, a, b) for (int i = a; i <= b; i++)
#define drp(i, a, b) for (int i = a; i >= b; i--)
#define INF 0x7fffffff

inline int read() {
    int x = 0; char ch = getchar(); while (!isdigit(ch))  ch = getchar();
    while (isdigit(ch)) x = (x << 1) + (x << 3) + ch - '0', ch = getchar(); return x;
}

int sa[N], t1[N], t2[N], c[N], n, m, height[N], rnk[N];
char s[N];

void getSA(int n, int m) {
    int *x = t1, *y = t2;
    rep(i, 0, m - 1) c[i] = 0;
    rep(i, 0, n - 1) c[x[i] = s[i]]++;
    rep(i, 1, m - 1) c[i] += c[i - 1];
    drp(i, n - 1, 0) sa[--c[x[i]]] = i;
    for (int k = 1; k <= n; k <<= 1) {
        int p = 0;
        rep(i, n - k, n - 1) y[p++] = i;
        rep(i, 0, n - 1) if (sa[i] >= k) y[p++] = sa[i] - k;
        rep(i, 0, m - 1) c[i] = 0;
        rep(i, 0, n - 1) c[x[y[i]]]++;
        rep(i, 1, m - 1) c[i] += c[i - 1];
        drp(i, n - 1, 0) sa[--c[x[y[i]]]] = y[i];
        swap(x, y);
        p = 1, x[sa[0]] = 0;
        rep(i, 1, n - 1) x[sa[i]] = y[sa[i - 1]] == y[sa[i]] && y[sa[i - 1] + k] == y[sa[i] + k] ? p - 1 : p++;
        if (p >= n) break;
        m = p;
    }
}

void getHeight(int n) {
    int j, k = 0;
    rep(i, 1, n) rnk[sa[i]] = i;
    for (int i = 0; i < n; height[rnk[i++]] = k)
        for (k ? k-- : 0, j = sa[rnk[i] - 1]; s[i + k] == s[j + k]; k++);
}

int main() {
    scanf("%d%d%s", &n, &m, s); s[n + 1] = 0;
    getSA(n + 1, 'z' + 1), getHeight(n);
    while (m--) {
        int a = read() - 1, b = read() - 1, c = read() - 1, d = read() - 1;
        int S = rnk[c], ans = 0, mn = INF;
        if (sa[S] >= a && sa[S] <= b) ans = max(ans, min(d - c + 1, b - sa[S] + 1));
        drp(i, S, 2) {
            if (height[i] <= ans) break;
            mn = min(mn, height[i]);
            if (sa[i - 1] >= a && sa[i - 1] <= b) ans = max(ans, min(min(mn, b - sa[i - 1] + 1), d - c + 1));
        }
        mn = INF;
        rep(i, S + 1, n) {
            if (height[i] <= ans) break;
            mn = min(mn, height[i]);
            if (sa[i] >= a && sa[i] <= b) ans = max(ans, min(min(mn, b - sa[i] + 1), d - c + 1));
        }
        printf("%d\n", ans);
    }
    return 0;
}