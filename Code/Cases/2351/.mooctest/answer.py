#include <iostream>
#include <cstdio>
using namespace std;

int n;
struct edge
{
    int nxt, to;
}ed[100010];
int head[50010], cnt;
inline void add(int x, int y){ed[++cnt]=(edge){head[x], y};head[x]=cnt;}
int siz[50010];
int f[50010];
int fat[50010];
int mx=1e9;

inline void dfs(int x, int fa)
{
    siz[x] = 1;
    for (register int i = head[x]; i; i = ed[i].nxt)
    {
        int to = ed[i].to;
        if (fa == to) continue;
        fat[to] = x;
        dfs(to, x);
        siz[x] += siz[to];
    }
}

int main()
{
    scanf("%d", &n);
    for (register int i = 1; i < n; i++)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        add(x, y), add(y, x);
    }
    dfs(1, 0);
    for (register int x = 1; x <= n; x ++)
    {
        int sum=0;
        for (register int i = head[x]; i; i = ed[i].nxt)
        {
            int to = ed[i].to;
            if (to == fat[x]) sum = max(sum, siz[1] - siz[x]);
            else sum = max(sum, siz[to]);
        }
        f[x] = sum;
        mx = min(mx, f[x]);
    }
    for (register int i = 1; i <= n; i ++)
    {
        if (f[i] == mx) printf("%d ", i);
    }
    return 0;
}