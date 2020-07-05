#include <cstdio>
#include <algorithm>
using namespace std;

const int INF = 0x7fffffff;
const int MQ = 500010;

int N, Q;
int faz[MQ], opt[MQ], a[MQ], b[MQ];
int Ans[MQ];

int eh[MQ], nxt[MQ], to[MQ], tot;
inline void ins(int x, int y) {
    nxt[++tot] = eh[x]; to[tot] = y; eh[x] = tot;
}

int B[MQ];
inline void Add(int i, int x) { for (; i <= N; i += i & -i) B[i] += x; }
inline int Qur(int i) { int A = 0; for (; i; i -= i & -i) A += B[i]; return A; }
inline int BS(int x) { int p = 0; for (int j = 1 << 18; j; j >>= 1) if ((p | j) <= N && B[p | j] <= x) x -= B[p |= j]; return p;}

void DFS(int u, int o, int x) {
    int ok = 1;
    if (o == 1) Add(x, 1);
    if (o == 2) {
        if (Qur(x) == Qur(x - 1)) ok = 0;
        else Add(x, -1);
    }
    if (o == 3) Ans[u] = Qur(x - 1);
    if (o == 4) Ans[u] = b[BS(x) + 1];
    if (o == 5) Ans[u] = b[BS(Qur(x - 1) - 1) + 1];
    if (o == 6) Ans[u] = b[BS(Qur(x)) + 1];

    for (int i = eh[u]; i; i = nxt[i])
        DFS(to[i], opt[to[i]], a[to[i]]);

    if (o == 1) Add(x, -1);
    if (o == 2 && ok) Add(x, 1);
}

int main() {
    scanf("%d", &Q);
    for (int i = 1; i <= Q; ++i) {
        scanf("%d%d%d", &faz[i], &opt[i], &a[i]);
        if (opt[i] != 4)
            b[++N] = a[i];
    } b[++N] = -INF, b[++N] = INF;
    sort(b + 1, b + N + 1);
    N = unique(b + 1, b + N + 1) - b - 1;
    for (int i = 1; i <= Q; ++i) {
        ins(faz[i], i);
        if (opt[i] != 4)
            a[i] = lower_bound(b + 1, b + N + 1, a[i]) - b;
    }
    Add(1, 1), Add(N, 1);
    DFS(0, 0, 0);
    for (int i = 1; i <= Q; ++i) {
        if(opt[i] > 2)
            printf("%d\n", Ans[i]);
    }
    return 0;
}