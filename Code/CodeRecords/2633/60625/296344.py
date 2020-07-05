#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
const int MAXN = 100010;
const int INF = 1061109567;
inline int Max(const int a, const int b){ return (a > b) ? a : b; }
inline int Min(const int a, const int b){ return (a < b) ? a : b; }
inline int read(){
    int x = 0; int w = 1; register char c = getchar();
    for(; c ^ '-' && (c < '0' || c > '9'); c = getchar());
    if(c == '-') w = -1, c = getchar();
    for(; c >= '0' && c <= '9'; c = getchar()) x = (x<<3) + (x<<1) + c - '0'; return x * w;
}
int N,M,opt,l,r,x,y;
int a[MAXN];
int val[MAXN<<2],lazy[MAXN<<2];
struct SegmentTree{
    inline void pushdown(int rt, int l, int r){
        if(lazy[rt]){
            int mid = (l+r)/2;
            val[rt<<1] += lazy[rt] * (mid-l+1);
            val[rt<<1|1] += lazy[rt] * (r-(mid+1)+1);
            lazy[rt<<1] += lazy[rt];
            lazy[rt<<1|1] += lazy[rt];
            lazy[rt] = 0;
        }
    }
    int query(int rt, int l, int r, int x, int y){
        if(l > y || r < x) return 0;
        if(x <= l && r <= y) return val[rt];
        pushdown(rt, l, r);
        int mid = (l+r)/2;
        return query(rt<<1,l,mid,x,y) + query(rt<<1|1,mid+1,r,x,y);
    }
    void update(int rt, int l, int r, int x, int y, int k){
        if(l > y || r < x) return;
        if(x <= l && r <= y){
            lazy[rt] += k;
            val[rt] += (r-l+1) * k;
            return;
        }
        pushdown(rt,l,r);
        int mid = (l+r)/2;
        update(rt<<1,l,mid,x,y,k), update(rt<<1|1,mid+1,r,x,y,k);
        val[rt] = val[rt<<1] + val[rt<<1|1];
    }
}qxz;
int main(){
    N = read(), M = read();
    for(int i = 1; i <= N; ++i){
        a[i] = read();
    }
    while(M--){
        opt = read();
        if(opt == 1){
            l = read(), r = read(), x = read(), y = read();
            qxz.update(1,1,N,l,l,x);
            qxz.update(1,1,N,l+1,r,y);
            qxz.update(1,1,N,r+1,r+1,-(x+y*(r-l)));
        }
        else{
            x = read();
            printf("%d\n", qxz.query(1,1,N,1,x)+a[x]);
        }
    }
    return 0;
}