#include <set>
#include <cstdio>
#include <cstring>
#include <iostream>
const int MAXN = 100001;
int n, s, cnt, ans;
int a[MAXN], head[MAXN], to[MAXN << 1], next[MAXN << 1], f[MAXN], sum[MAXN];
std::set <int> S;
inline int read()
{
    int x = 0, f = 1;
    char ch = getchar();
    for(; !isdigit(ch); ch = getchar()) if(ch == '-') f = -1;
    for(; isdigit(ch); ch = getchar()) x = (x << 1) + (x << 3) + ch - '0';
    return x * f;
}
inline void add(int x, int y)
{
    to[cnt] = y;
    next[cnt] = head[x];
    head[x] = cnt++;
}
inline void dfs(int u)
{
    sum[u] = sum[f[u]] + a[u];
    S.insert(sum[u]);
    if(S.count(sum[u] - s)) ans++;
    for(int i = head[u]; i ^ -1; i = next[i]) dfs(to[i]);    
    S.erase(sum[u]);
}
int main()
{
    int i, x, y;
    n = read();
    s = read();
    memset(head, -1, sizeof(head));
    for(i = 1; i <= n; i++) a[i] = read();
    for(i = 1; i < n; i++)
    {
        x = read();
        y = read();
        f[y] = x;
        add(x, y);
    }
    S.insert(0);
    dfs(1);
    printf("%d\n", ans);
    return 0;
}