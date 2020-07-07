#include <bits/stdc++.h>
using namespace std;
inline void read(register int &x){
    x = 0; register int f = 1;
    register char ch = getchar();
    while (!(ch >= '0' && ch <= '9')){if (ch == '-') f = -1; ch = getchar();}
    while (ch >= '0' && ch <= '9'){x = x * 10 + ch - '0'; ch = getchar();}
    x *= f;
}
const int N = 10000 + 10;
const int M = 20000 + 10;
int n, m;
int p[N], e_num, d1[N], d2[N], prt[N];
struct Edge{int b, nt, w;} e[M];
inline void anode(register int u, register int v, register int w){
    e[++e_num].b = v;
    e[e_num].w = w;
    e[e_num].nt = p[u];
    p[u] = e_num;
}

inline void dfs(register int u){
    for (register int edge = p[u]; edge > 0; edge = e[edge].nt){
        register int v = e[edge].b;
        if (v != prt[u]){//v不是u的父节点，就一定是u的儿子节点
            prt[v] = u;//记录父节点
            dfs(v);
            register int a = d1[v] + e[edge].w;//当前点u到以v为根的子树的最大距离
            if (a > d1[u]){
                d2[u] = d1[u]; d1[u] = a;
            }
            else if (a > d2[u]) d2[u] = a;
        }
    }
}

int main(){
    read(n);
    for (register int i = 1; i < n; i++){
        register int u, v; read(u), read(v);
        anode(u, v, 1); anode(v, u, 1);//这里边权都设置为1，根据题意而定
    }
    dfs(1);
    register int ans = 0;
    for (register int i = 1; i <= n; i++) ans = max(ans, d1[i] + d2[i]);
    printf("%d\n", ans);
    return 0;
}