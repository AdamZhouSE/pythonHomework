#include<bits/stdc++.h>
using namespace std;
#define MAXN 3005
#define MAXM 8005
 
int n, p, r;
int hd[MAXN], nxt[MAXM], to[MAXM], tot(1);
int dfn[MAXN], low[MAXN], num, stk[MAXN], tp, c[MAXN], cnt;
int pr[MAXN], f[MAXN];
int x, y;
bool vs[MAXN], v[MAXN];
 
void Add( int x, int y){ nxt[++tot] = hd[x]; hd[x] = tot; to[tot] = y; }
 
void Tarjan( int x ){
    dfn[x] = low[x] = ++tot; stk[++tp] = x;
    for ( int i = hd[x]; i; i = nxt[i] ){
        if ( !dfn[to[i]] ) Tarjan( to[i] ), low[x] = min( low[x], low[to[i]] );
        else if ( !c[to[i]] ) low[x] = min( low[x], dfn[to[i]] );
    }
    if ( low[x] == dfn[x] ){
        c[x] = ++cnt; f[cnt] = pr[x];
        while( stk[tp] != x ) f[cnt] = min( f[cnt], pr[stk[tp]] ), c[stk[tp--]] = cnt;
        tp--;
    }
}
 
//记忆化搜索
//Memory search 
void DFS( int x ){
    v[x] = 1;
    for ( int i = hd[x]; i; i = nxt[i] )
        if ( !v[to[i]] ) DFS( to[i] );
}
 
int main(){
    scanf( "%d%d", &n, &p );
    for ( int i = 1; i <= n; ++i ) pr[i] = INT_MAX;
    for ( int i = 1; i <= p; ++i ) scanf( "%d%d", &x, &y ), pr[x] = y;
    scanf( "%d", &r );
    for ( int i = 1; i <= r; ++i ) scanf( "%d%d", &x, &y ), Add( x, y );
    
    // 先判断是否能控制全部间谍,即把所有能收买的间谍都收买
    // To see whether all spies can be under control. 
    for ( int i = 1; i <= n; ++i ) if ( pr[i] < INT_MAX && !v[i] ) DFS( i );
    for ( int i = 1; i <= n; ++i ) if ( !v[i] ){ printf( "NO\n%d\n", i ); return 0; }
    //------------------判断结束 Ended--------------------
    //因为已经确定所有间谍都能被控制,那就大胆地取来所有入度为0的节点(当然,是缩点后的图)
    // Because all spies can be controled, get all ponits which has no indegree(After Tarjan, certainly).
    for ( int i = 1; i <= n; ++i ) if ( !c[i] ) Tarjan( i );
    //当然, 并不需要建边，可以直接判断入度是否为0
    //Certainly, it is unnecessary to connect edges.You can DIRECTLY know whether a point has no indegree.
    for ( int i = 1; i <= n; ++i )
        for ( int j = hd[i]; j; j = nxt[j] )
            if ( c[i] != c[to[j]] ) vs[c[to[j]]] = 1;
    int ans(0); 
    for ( int i = 1; i <= cnt; ++i ) if ( !vs[i] ) ans += f[i];
    printf( "YES\n%d\n", ans );
    return 0;
}