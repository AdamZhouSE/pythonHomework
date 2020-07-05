#include <bits/stdc++.h>
using namespace std;

int cost[3000][3000];
int d[2505];
int vis[2505];
int main()
{
    memset(cost ,0x3f ,sizeof(cost));
    memset(vis, 0, sizeof(vis));
    
    int n, m, s, t;
    scanf("%d%d%d%d", &n, &m, &s, &t);
    for (int i = 0; i < m; i++) {
        int s0, t0, w0;
        scanf("%d%d%d", &s0, &t0, &w0);
        cost[s0][t0] = min(cost[s0][t0], w0);
        cost[t0][s0] = min(cost[t0][s0], w0);
    }
    memset(d, 0x3f, sizeof(d));
    d[s] = 0;
    
    while (1) {
        int v = -1;
        for (int i = 1; i <= n; i++) {
            if (vis[i]==0 && (v==-1||d[i]<d[v])) v = i;
        }
        
        if (v==-1) break;
        vis[v] = 1;
        
        for (int i = 1; i <= n; i++)
            d[i] = min(d[i], d[v]+cost[v][i]);
    }
    
    printf("%d", d[t]);
    
    return 0;    
} 