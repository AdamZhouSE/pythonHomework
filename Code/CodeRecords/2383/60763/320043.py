# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
# include <cmath>
# define R register
# define LL long long

using namespace std;

int n,k,e,h[100010],x,y,T,siz[100010],tot;
struct zx{int v,pre;}ed[200010];

template <typename T> void in(R T& a){
    R char c = getchar();R T x=0,f=1;
    while(!isdigit(c)) {if(c == '-') f = -1; c = getchar();}
    while(isdigit(c)) x = (x<<1)+(x<<3)+c-'0',c = getchar();
    a = x*f;
}

inline void add(R int x,R int y){
    ed[++e] = (zx){y,h[x]};
    h[x] = e;
}

inline void dfs(R int x,R int fa){
    siz[x] = 1;
    for(R int i=h[x]; i; i=ed[i].pre){
        R int p = ed[i].v;
        if(p == fa) continue;
        dfs(p,x);
        siz[x] += siz[p];
    }
    if(siz[x]==k) tot++,siz[x] -= k;
}

int main(){
//     freopen("sample.in","r",stdin);
//     freopen("sample.out","w",stdout);
    in(T);
    while(T--)
    {
        in(n),in(k);
        e=tot=0;
        memset(siz,0,sizeof(siz));
        memset(h,0,sizeof(h));
        for(R int i=1; i<n; ++i)
        {
            in(x),in(y);
            add(x,y);
            add(y,x);
        }
        if(n%k != 0) {printf("NO\n");continue;}
        dfs(1,-1);
        if(tot == n/k) printf("YES\n");
        else printf("NO\n");
    }
}