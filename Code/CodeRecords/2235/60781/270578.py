#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;
const int N=8005*2,M=20005*2;
struct Gragh{
    int cnt,y[M],nxt[M],fst[N];
    void clear(){
        cnt=0;
        memset(fst,0,sizeof fst);
    }
    void add(int a,int b){
        y[++cnt]=b,nxt[cnt]=fst[a],fst[a]=cnt;
    }
}g;
int n,m;
int st[N],top,vis[N];
int opp(int x){
    return x+(x%2==0?-1:1);
}
bool dfs(int x){
    if (vis[opp(x)])
        return 0;
    if (vis[x])
        return 1;
    vis[x]=1;
    st[++top]=x;
    for (int i=g.fst[x];i;i=g.nxt[i])
        if (!dfs(g.y[i]))
            return 0;
    return 1;
}
bool Two_sat(int n){
    memset(vis,0,sizeof vis);
    for (int i=1;i<=n;i+=2){
        if (vis[i]||vis[opp(i)])
            continue;
        top=0;
        if (!dfs(i)){
            while (top)
                vis[st[top--]]=0;
            if (!dfs(opp(i)))
                return 0;
        }
    }
    return 1;
}
int main(){
    while (~scanf("%d%d",&n,&m)){
        g.clear();
        for (int i=1,a,b;i<=m;i++){
            scanf("%d%d",&a,&b);
            g.add(a,opp(b));
            g.add(b,opp(a));
        }
        if (Two_sat(n*2)){
            for (int i=1;i<=2*n;i++)
                if (vis[i])
                    printf("%d\n",i);
        }
        else
            printf("NIE\n");
    }
    return 0;
}