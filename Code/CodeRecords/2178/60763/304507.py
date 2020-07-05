#include<cstdio>
#include<map>
#define Rint register int
using namespace std;
typedef long long LL;
const int N = 200003;
int n, now;
LL ans;
namespace SAM {
    map<int, int> ch[N];
    int last = 1, cnt = 1, l[N], fa[N];
    inline void ins(int c){
        int p = last, np = ++ cnt; last = np; l[np] = l[p] + 1;
        for(;!ch[p][c];p = fa[p]) ch[p][c] = np;
        if(!p) fa[np] = 1;
        else {
            int q = ch[p][c];
            if(l[q] == l[p] + 1) fa[np] = q;
            else {
                int nq = ++ cnt;
                l[nq] = l[p] + 1; ch[nq] = ch[q];
                fa[nq] = fa[q]; fa[q] = fa[np] = nq;
                for(;ch[p][c] == q;p = fa[p]) ch[p][c] = nq;
            }
        }
        ans += l[np] - l[fa[np]];
    }
}
int main(){
    scanf("%d", &n);
    for(Rint i = 1;i <= n;i ++){
        scanf("%d", &now);
        SAM :: ins(now);
        printf("%lld\n", ans);
    }
}