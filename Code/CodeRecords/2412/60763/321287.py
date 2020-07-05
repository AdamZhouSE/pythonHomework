#include <bits/stdc++.h>
#define LL long long
#define fr(i, x, y) for (int i = (x); i <= (y); i++)
#define rf(i, x, y) for (int i = (x); i >= (y); i--)
#define frl(i, x, y) for (int i = (x); i < (y); i++)
using namespace std;
const int N = 200002;
int n, s, a[N], c[N];
int tot, cnt;
int b[N], use[N];
map<int, int> mp;
int v[N], p[N];

void read(int &x) {  // scanf("%d",&x);
    char ch = getchar();
    x = 0;
    for (; ch < '0' || ch > '9'; ch = getchar())
        ;
    for (; ch >= '0' && ch <= '9'; ch = getchar()) x = (x << 3) + (x << 1) + ch - '0';
}

void prt(int o) {
    int x = p[o];
    for (printf("%d ", o); x != o; x = p[x]) printf("%d ", x);
}
void init() {
    sort(c + 1, c + 1 + n);
    for (map<int, int>::iterator it = mp.begin(); it != mp.end(); it++) it->second = ++tot;
    fr(i, 1, n) a[i] = mp[a[i]], c[i] = mp[c[i]];
    // fr(i,1,n) v[a[i]].push_back(i);
}

int f[N], sz[N];
int gf(int x) { return f[x] == x ? x : f[x] = gf(f[x]); }
void unio(int x, int y) {
    int fx = gf(x), fy = gf(y);
    if (fx != fy)
        f[fx] = fy, sz[fy] += sz[fx];
}

int main() {
    read(n);
    read(s);
    fr(i, 1, n) read(a[i]), c[i] = a[i], mp[a[i]]++;
    init();

    fr(i, 1, n) if (c[i] != c[i - 1]) use[c[i]] = i;
    fr(i, 1, n) f[i] = i, sz[i] = 1;
    fr(i, 1, n) if (a[i] != c[i] && !b[i]) {
        int x = i;  // use[a[x]]
        while (!b[x] && c[use[a[x]]] == a[x]) {
            b[x] = 1;
            int &w = use[a[x]];
            while (c[w] == a[w] && c[w] == a[x]) w++;
            if (c[w] != a[x])
                break;
            unio(x, w);
            p[x] = w;
            x = w++;
        }
        // p[x]=i;
    }

    memset(b, 0, sizeof b);
    fr(i, 1, n) if (a[i] != c[i]) {
        if (!b[a[i]])
            b[a[i]] = i;
        else {
            int x = b[a[i]], fx = gf(x), fy = gf(i);
            if (fx != fy)
                swap(p[x], p[i]), unio(fx, fy);
        }
    }

    int sum = 0;
    fr(i, 1, n) if (a[i] != c[i]) sum++;
    if (s < sum)
        return printf("-1\n"), 0;
    s -= sum;

    fr(i, 1, n) if (a[i] != c[i] && f[i] == i) v[++cnt] = i;

    if (cnt <= 1 || s <= 2) {
        printf("%d\n", cnt);
        fr(o, 1, cnt) {
            printf("%d\n", sz[v[o]]);
            prt(v[o]);
            puts("");
        }
    } else {
        s = min(s, cnt);
        printf("%d\n", cnt - (s - 1) + 1);
        int sum = 0;
        fr(i, 1, s) sum += sz[v[i]];
        printf("%d\n", sum);
        fr(i, 1, s) prt(v[i]);
        puts("");
        printf("%d\n", s);
        rf(i, s, 1) printf("%d ", v[i]);
        puts("");
        fr(i, s + 1, cnt) printf("%d\n", sz[v[i]]), prt(v[i]);
    }
    return 0;
}

/*
10 13
1 2 1 2 3 4 3 4 5 6

9 100
4 1 2 3 6 5 8 9 7
*/