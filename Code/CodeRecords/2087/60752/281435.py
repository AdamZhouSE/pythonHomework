#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>
using namespace std;
#define LL long long
 
LL read() {
    LL x = 0, f = 1; char c = getchar();
    while(!isdigit(c)){ if(c == '-') f = -1; c = getchar(); }
    while(isdigit(c)){ x = x * 10 + c - '0'; c = getchar(); }
    return x * f;
}

#define maxn 510
#define maxm 500010
#define oo 2147483647
 
struct Edge {
    int from, to, flow;
    Edge() {}
    Edge(int _1, int _2, int _3): from(_1), to(_2), flow(_3) {}
};
struct Dinic {
    int n, m, s, t, head[maxn], nxt[maxm];
    Edge es[maxm];
    int vis[maxn], Q[maxn], hd, tl;
    int cur[maxn];
     
    void init() {
        m = 0; memset(head, -1, sizeof(head));
        return ;
    }
    void setn(int _) { n = _; return ; }
     
    void AddEdge(int a, int b, int c) {
        es[m] = Edge(a, b, c); nxt[m] = head[a]; head[a] = m++;
        es[m] = Edge(b, a, 0); nxt[m] = head[b]; head[b] = m++;
        return ;
    }
     
    bool BFS() {
        memset(vis, 0, sizeof(vis));
        vis[s] = 1;
        hd = tl = 0; Q[++tl] = s;
        while(hd < tl) {
            int u = Q[++hd];
            for(int i = head[u]; i != -1; i = nxt[i]) {
                Edge& e = es[i];
                if(e.flow && !vis[e.to]) {
                    vis[e.to] = vis[u] + 1;
                    Q[++tl] = e.to;
                }
            }
        }
        return vis[t] > 0;
    }
    int DFS(int u, int a) {
        if(u == t || !a) return a;
        int flow = 0, f;
        for(int& i = cur[u]; i != -1; i = nxt[i]) {
            Edge& e = es[i];
            if(vis[e.to] == vis[u] + 1 && (f = DFS(e.to, min(a, e.flow)))) {
                flow += f; a -= f;
                e.flow -= f; es[i^1].flow += f;
                if(!a) return flow;
            }
        }
        return flow;
    }
    int MaxFlow(int _s, int _t) {
        s = _s; t = _t;
        int flow = 0;
        while(BFS()) {
            for(int i = 1; i <= n; i++) cur[i] = head[i];
            flow += DFS(s, oo);
        }
        return flow;
    }
} sol;
 
LL A[maxn];
LL gcd(LL a, LL b) { return b ? gcd(b, a % b) : a; }
 
int main() {
    int n = read();
    for(int i = 1; i <= n; i++) A[i] = read();
     
    sol.init();
    for(int i = 1; i <= n; i++)
        for(int j = i + 1; j <= n; j++)
            if(gcd(A[i], A[j]) == 1 && gcd(A[i] + 1, A[j] + 1) == 1) {
                int a = i, b = j;
                if(A[a] & 1) swap(a, b);
                sol.AddEdge(a, b, 1); // even -> odd
            }
    int s = n + 1, t = n + 2;
    for(int i = 1; i <= n; i++)
        if(A[i] & 1) sol.AddEdge(i, t, 1);
        else sol.AddEdge(s, i, 1);
     
    sol.setn(n + 2);
    cout<< n - sol.MaxFlow(s, t);
     
    return 0;
}