
#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, t) for(int i = (s), mi = (t); i <= mi; i++)
#define dwn(i, s, t) for(int i = (s), mi = (t); i >= mi; i--)
 
int read() {
    int x = 0, f = 1; char c = getchar();
    while(!isdigit(c)){ if(c == '-') f = -1; c = getchar(); }
    while(isdigit(c)){ x = x * 10 + c - '0'; c = getchar(); }
    return x * f;
}
 
#define maxn 10010
#define maxm 40010
 
int n, m, head[maxn], nxt[maxm], to[maxm], deg[maxn];
 
void AddEdge(int a, int b) {
    to[++m] = b; nxt[m] = head[a]; head[a] = m;
    swap(a, b);
    to[++m] = b; nxt[m] = head[a]; head[a] = m;
    deg[a]++; deg[b]++;
    return ;
}
 
vector <int> con[maxn];
int fa[maxn];
int findset(int x) { return x == fa[x] ? x : fa[x] = findset(fa[x]); }
 
int col[maxn];
int dfs(int u, int c) {
    col[u] = c;
    for(int e = head[u]; e; e = nxt[e]) if(col[to[e]] && col[to[e]] == c) return -1;
    for(int e = head[u]; e; e = nxt[e]) if(!col[to[e]]) {
        if(dfs(to[e], 3 - c) < 0) return -1;
    }
    return 0;
}
 
int Q[maxn], hd, tl, step[maxn];
bool vis[maxn];
bool judge(int c) {
    if(con[c].size() == 1) return 1;
    
    hd = tl = 0;
    rep(i, 0, (int)con[c].size() - 1) {
        int u = con[c][i];
        if(deg[u] == 1) Q[++tl] = u, vis[u] = 1;
    }
    while(hd < tl) {
        int u = Q[++hd];
        for(int e = head[u]; e; e = nxt[e]) if(--deg[to[e]] == 1) Q[++tl] = to[e], vis[to[e]] = 1;
    }
    
    int s = -1, t = -1;
    rep(i, 0, (int)con[c].size() - 1) {
        int u = con[c][i];
        if(vis[u]) continue;
        assert(deg[u] > 1);
        if(deg[u] == 2) continue;
        if(deg[u] > 3) return 0;
        if(s < 0) s = u;
        else if(t < 0) t = u;
        else return 0;
    }
    if(s < 0) return 1;
    
    int two = 0, even = 0;
    hd = tl = 0; Q[++tl] = s; step[s] = 0;
    while(hd < tl) {
        int u = Q[++hd];
        for(int e = head[u]; e; e = nxt[e]) if(!vis[to[e]]) {
            step[to[e]] = step[u] + 1;
            if(to[e] == t) {
                if(step[to[e]] == 2 && two < 2) two++;
                else if(step[to[e]] & 1) return 0;
                else even++;
            }
            else vis[to[e]] = 1, Q[++tl] = to[e];
        }
    }
    if(two == 2 && even == 1) return 1;
    return 0;
}
void work() {
    int n = read(), M = read();
    m = 0; memset(head, 0, sizeof(head));
    memset(deg, 0, sizeof(deg));
    rep(i, 1, n) fa[i] = i, con[i].clear();
    rep(i, 1, M) {
        int a = read(), b = read();
        AddEdge(a, b);
        int u = findset(a), v = findset(b);
        if(u != v) fa[v] = u;
    }
    if(n <= 2) return (void)puts("YES");
    
    rep(i, 1, n) con[findset(i)].push_back(i);
    
    memset(col, 0, sizeof(col));
    memset(vis, 0, sizeof(vis));
    memset(step, 0, sizeof(step));
    rep(i, 1, n) if(!col[i]) {
        if(dfs(i, 1) < 0) return (void)puts("NO");
        if(!judge(findset(i))) return (void)puts("NO");
    }
    puts("YES");
    return ;
}
 
int main() {
    freopen("color.in", "r", stdin);
    freopen("color.out", "w", stdout);
    
    int T = read();
    while(T--) work();
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}