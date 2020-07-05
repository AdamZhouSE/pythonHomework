#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll ans; 
int n , m , S , T;
int linkk[110] , t;
int dep[110];
bool flag;
const ll oo = 1000000000000000000LL;
struct node{
    int n , y , v;
}e[100100];
int read()
{
    int sum = 0;char c = getchar();bool flag = true;
    while( c < '0' || c > '9' ) {if(c == '-') flag = false;c = getchar();}
    while( c >= '0' && c <= '9' ) sum = sum * 10 + c - 48 , c = getchar();
    if(flag)  return sum;
     else return -sum;
}  
void insert(int x,int y,int z)
{
    e[++t].y = y;e[t].n = linkk[x];e[t].v = z;linkk[x] = t;
    e[++t].y = x;e[t].n = linkk[y];e[t].v = 0;linkk[y] = t;
}
void init()
{
    t = 1;
    n = read();m = read();S = n + 1;T = n + 2;
    for(int i = 1;i <= m;++i) insert(S,i,1);
    for(int i = m + 1;i <= n;++i) insert(i,T,1);
    int a,b;
    while(scanf("%d",&a) != EOF)
    {
        b = read();
        insert(a,b,1);
    }
    return;
}
ll dfs(int x,ll lazy)
{
    if(x == T) return lazy;
    ll nowlazy = 0;
    ll d = 0;
    for(int i = linkk[x];i&&nowlazy < lazy;i = e[i].n)
    {
        int y = e[i].y;
        if(dep[y] == dep[x] + 1 && e[i].v > 0)
            if(d = dfs(y,min(1ll*e[i].v , lazy - nowlazy)))
            {
                nowlazy += d;
                e[i].v -= d;
                e[i^1].v += d; 
            }
    }
    if(nowlazy == 0) dep[x] = -1;
    return nowlazy;
}
queue<int>q;
bool bfs()
{
    memset(dep,-1,sizeof(dep));
    dep[S] = 0;q.push(S);
    while(q.size())
    {
        int v = q.front();
        for(int i = linkk[v];i;i = e[i].n)
            if(dep[e[i].y] == -1 && e[i].v > 0) 
                dep[e[i].y] = dep[v] + 1,q.push(e[i].y);
        q.pop();
    }
    if(dep[T] == -1) return false;
    return true;
}
int main()
{
    init();
    while(bfs())
    {       
        ll d;
        while(d = dfs(S,oo)) ans += d;
    }
    printf("%lld\n",ans);
    return 0;
} 
