#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define ZERO (1e-10)
#define INF int(1e9 + 1)
#define CL(A, I) (memset(A, I, sizeof(A)))
#define DEB printf("DEB!\n");
#define D(X) cout << "  " << #X ": " << X << endl;
#define EQ(A, B) (A + ZERO > B && A - ZERO < B)
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define IN(n) \
    int n;    \
    scanf("%d", &n);
#define FOR(i, m, n) for (int i(m); i < n; i++)
#define F(n) FOR(i, 0, n)
#define FF(n) FOR(j, 0, n)
#define FT(m, n) FOR(k, m, n)
#define aa first
#define bb second
void ga(int N, int *A) { F(N) scanf("%d", A + i); }
#define MX (1024)
#define AG(I) (atan2(Y[I] - y, X[I] - x))
vi g[MX];
int N, a, b, X[MX], Y[MX], A[MX], S[MX], x, y;
int ori(int u, int p) {
    S[u] = 1;
    F((int)g[u].size()) if (g[u][i] == p) g[u][i] = g[u].back(), g[u].pop_back(), --i;
    else S[u] += ori(g[u][i], u);
    return S[u];
}
bool cp(int a, int b) { return X[a] ^ X[b] ? X[a] < X[b] : Y[a] < Y[b]; }
bool ca(int a, int b) { return AG(a) < AG(b); }
void dfs(int u, int *A) {
    static int B[MX];
    int I = 0, M = 0, J = 0, U = *A;
    x = X[U], y = Y[U];
    FT(1, S[u]) B[M++] = A[k];
    sort(B, B + M, ca);
    FT(1, M) if (AG(B[k]) - AG(B[k - 1]) > M_PI) J = k;
    F(M) A[i] = B[(J + i) % M];
    for (auto &h : g[u]) printf("%d %d\n", U, A[I]), dfs(h, A + I), I += S[h];
}
int main(void) {
    scanf("%d", &N), iota(A, A + N, 0);
    F(N - 1) scanf("%d%d", &a, &b), g[a].PB(b), g[b].PB(a);
    F(N) scanf("%d%d", X + i, Y + i);
    ori(0, 0), sort(A, A + N, cp);
    dfs(0, A);
    return 0;
}