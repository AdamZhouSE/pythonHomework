#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#define ll long long
using namespace std;

const int N = 200010;

struct task { int l, r; };
struct fhq { int l, r, siz, rnd; task v; }t[N];
int tot, root;

#define lc (t[rt].l)
#define rc (t[rt].r)
void up(int rt) { t[rt].siz = t[lc].siz + t[rc].siz + 1; } 
void split(int rt, int &l, int &r, int k) {
    if(!k) l = 0, r = rt;
    else if(t[rt].siz == k) l = rt, r = 0;
    else if(k <= t[lc].siz) r = rt, split(lc, l, lc, k), up(rt);
    else l = rt, split(rc, rc, r, k - t[lc].siz - 1), up(rt);
}
void merge(int &rt, int l, int r) {
    if(!l || !r) rt = l + r;
    else if(t[l].rnd < t[r].rnd) rt = l, merge(rc, rc, r), up(rt);
    else rt = r, merge(lc, l, lc), up(rt);
}
int pre(int rt, task a) {
    if(!rt) return 0;
    if(t[rt].v.r < a.l) return pre(rc, a) + t[lc].siz + 1;
    else return pre(lc, a);
}
int nxt(int rt, task a) {
    if(!rt) return 0;
    if(t[rt].v.l > a.r) return nxt(lc, a);
    else return nxt(rc, a) + t[lc].siz + 1;
}
int new_node(task a) {
    t[++tot].v = a;
    t[tot].siz = 1;
    t[tot].rnd = rand()<<15|rand();
    t[tot].l = t[tot].r = 0;
    return tot;
}
int build(task a) {
    int l = pre(root, a), r = nxt(root, a), x, y, z, k;
    split(root, x, y, r); split(x, z, k, l);
    int ans = t[k].siz, t = new_node(a);
    merge(t, z, t); merge(root, t, y); return ans;
}
#undef lc
#undef rc

int main() {
#ifndef ONLINE_JUDGE
freopen("test.in","r",stdin);
freopen("t.out","w",stdout);
#endif
    srand((unsigned)time(0));
    int T; task a; char ch[10];
    scanf("%d", &T);
    while(T--) {
        scanf("%s", ch);
        if(ch[0] == 'A') scanf("%d%d", &a.l, &a.r), printf("%d\n", build(a));
        else printf("%d\n", t[root].siz);
    }
    return 0;
}