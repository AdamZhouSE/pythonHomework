#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
const int inf = 0x3f3f3f3f;
const int N = 2000005;
queue<int> q;
int n, m, dis[N], v[N];
char s[25];
struct node {
    int t, b1, b2, f1, f2;
    node(int b1 = 0, int b2 = 0, int f1 = 0, int f2 = 0) : b1(b1), b2(b2), f1(f1), f2(f2){};
} a[105];
inline int read() {
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9') {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        x = (x << 3) + (x << 1) + (ch ^ 48);
        ch = getchar();
    }
    return x * f;
}
int spfa() {
    for (int i = 0; i < (1 << n); i++) dis[i] = inf;
    dis[(1 << n) - 1] = 0;
    q.push((1 << n) - 1);
    v[(1 << n) - 1] = 1;
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        v[x] = 0;
        for (int i = 1; i <= m; i++) {
            if (((x & a[i].b1) != a[i].b1) || ((x & a[i].b2) != 0))
                continue;
            int y = ((x & (~a[i].f1)) | a[i].f2);
            if (dis[y] > dis[x] + a[i].t) {
                dis[y] = dis[x] + a[i].t;
                if (!v[y]) {
                    q.push(y);
                    v[y] = 1;
                }
            }
        }
    }
    return dis[0] == inf ? 0 : dis[0];
}
int main() {
    n = read();
    m = read();
    for (int i = 1, x; i <= m; i++) {
        a[i].t = read();
        scanf("%s", s + 1);
        x = strlen(s + 1);
        for (int j = 1; j <= x; j++)
            if (s[j] == '+')
                a[i].b1 |= (1 << (j - 1));
            else if (s[j] == '-')
                a[i].b2 |= (1 << (j - 1));
        scanf("%s", s + 1);
        x = strlen(s + 1);
        for (int j = 1; j <= x; j++)
            if (s[j] == '+')
                a[i].f2 |= (1 << (j - 1));
            else if (s[j] == '-')
                a[i].f1 |= (1 << (j - 1));
    }
    printf("%d\n", spfa());
    return 0;
}