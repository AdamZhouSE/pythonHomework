#include <bits/stdc++.h>
#define N 100010
using namespace std;
int n, s, tot, en, x, y;
int a[N], head[N];
struct Edge{
    int to, next;
}e[N << 1];
//读入优化
inline int get_num()
{
    int now = 0;
    bool fh = false;
    char ch = getchar();
    while(ch < '0' || ch > '9'){
        if(ch == '-') fh = true;
        ch = getchar();
    }
    while(ch >= '0' && ch <= '9'){
        now = (now << 1) + (now << 3) + ch - '0';
        ch = getchar();
    }
    return (fh == true ? - now : now);
}
bool ans = false;
//ans记录是否搜到小于s的路径，false为搜到小于s的路径
inline void dfs(int now, int tmp)
{
    if(tmp == s){
        ans = true;
        ++tot;
        return;
    }else if(tmp > s){
        ans = true;
        return;//注意这个剪枝！！！！！
    }else for(int i = head[now]; i; i = e[i].next){
        dfs(e[i].to, tmp + a[e[i].to]);
    }
}
inline void mdfs(int now)
{
    for(int i = head[now]; i; i = e[i].next){//使用两个dfs嵌套，便于理解
        ans = false;
        dfs(e[i].to, a[e[i].to]);
        if(ans == false) continue;
        mdfs(e[i].to);
    }
}
int main()
{
    n = get_num(), s = get_num();
    for(register int i = 1; i <= n; ++i){
        a[i] = get_num();
    }
    for(register int i = 1; i < n; ++i){
        x = get_num(), y = get_num();//注意这里是单向边
        e[++en].to = y;
        e[en].next = head[x];
        head[x] = en;
    }
    dfs(1, a[1]);
    ans = false;
    mdfs(1);
    printf("%d\n", tot);
    return 0;
}