#include <bits/stdc++.h>

#define I inline
#define fi first
#define se second
#define R register
#define LL long long
#define mp make_pair
#define reg register int
#define pii pair<int, int>
#define cr const reg &
using namespace std;
const int inf = 2147483647;
const int N = 1e3 + 1;

I int _max(cr x, cr y) { return x > y ? x : y; }
I int _min(cr x, cr y) { return x < y ? x : y; }
I int read() {
    reg x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9') {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') x = (x << 3) + (x << 1) + (ch ^ 48), ch = getchar();
    return x * f;
}
I void ptt(cr x) {
    if (x >= 10)
        ptt(x / 10);
    putchar(x % 10 + '0');
}
I void put(cr x) { x < 0 ? putchar('-'), ptt(-x) : ptt(x); }
I void pr1(cr x) { put(x), putchar(' '); }
I void pr2(cr x) { put(x), puts(""); }

struct node {
    int x, y, id;
} a[N], b[N];
struct edge {
    int x, y, next;
} e[N];
int len, last[N];
vector<pii> ans;
int tot[N], sx, sy;

I void ins(reg x, reg y) {
    e[++len].x = x, e[len].y = y;
    e[len].next = last[x], last[x] = len;
}

bool cmp(node a, node b) { return atan2(a.x - sx, a.y - sy) < atan2(b.x - sx, b.y - sy); }

void dfs(cr x, cr fa) {
    tot[x] = 1;
    for (reg k = last[x]; k; k = e[k].next) {
        reg y = e[k].y;
        if (y ^ fa)
            dfs(y, x), tot[x] += tot[y];
    }
}

int bt(cr x, cr fa, node *A) {
    reg len = tot[x];
    for (reg i = 1; i < len; i++) {
        if (A[i].x < A[0].x)
            swap(A[0], A[i]);
        else if (A[i].x == A[0].x && A[i].y < A[0].y)
            swap(A[0], A[i]);
    }
    reg now = A[0].id;
    sx = A[0].x, sy = A[0].y;
    sort(A + 1, A + len, cmp);
    reg l = 1;
    for (reg k = last[x]; k; k = e[k].next) {
        reg y = e[k].y;
        if (y ^ fa) {
            reg uu = bt(y, x, A + l);
            l += tot[y];
            ans.push_back(pii{ now, uu });
        }
    }
    return now;
}

int main() {
    reg n = read();
    for (reg i = 1; i < n; i++) {
        reg x = read(), y = read();
        ins(x, y), ins(y, x);
    }
    for (reg i = 0; i < n; i++) a[i].x = read(), a[i].y = read(), a[i].id = i;
    dfs(0, -1);
    bt(0, -1, a);
    for (reg i = 0; i < n - 1; i++) pr1(ans[i].fi), pr2(ans[i].se);
    return 0;
}