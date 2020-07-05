#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<queue>
#include<set>
#include<map>
#define maxn 40004
using namespace std;
typedef long long ll;
int read() {
	int x = 0, f = 1, ch = getchar();
	while(!isdigit(ch)) {if(ch == '-') f = -1; ch = getchar();}
	while(isdigit(ch)) x = (x << 1) + (x << 3) + ch - '0', ch = getchar();
	return x * f;
}
 
int n, tot = 0;
struct node {
	int l, r, x;
	bool operator < (const node &a) const {return x < a.x;}
}q[maxn];
 
set<int> st;
map<int, int> dfn, raw;
 
int tree[maxn << 4];//这里可能不用开这么大……但是开8倍爆掉了 
bool flag[maxn << 4];
void change(int p, int l, int r, int ls, int rs, int x) {
	if(tree[p]) tree[p << 1] = tree[p << 1 | 1] = tree[p];//如果有值，就传下去 
	
	if(ls <= l && r < rs) {tree[p] = x; return;}//类似于区间查询。直接区间赋值。 
	if(l == r) return;//因为本题是左闭右开所以会有l==r死循环的情况…… 
	int mid = l + r >> 1;
	if(ls <= mid) change(p << 1, l, mid, ls, rs, x);
	if(rs > mid) change(p << 1 | 1, mid + 1, r, ls, rs, x);
	tree[p] = 0;//下传后清空 
}
 
ll ans = 0;
void ask(int p, int l, int r) {
	if(tree[p]) {ans += (raw[r + 1] - raw[l]) * 1ll * tree[p]; return;} 
	//找到值了，ans累加。为什么是r+1的位置减去l的位置， 读者可以画个数轴思考一下 。 
	if(!tree[p] && l == r) return;//防止意外死循环 
	int mid = l + r >> 1;
	ask(p << 1, l, mid);
	ask(p << 1 | 1, mid + 1, r);
}
 
signed main() {
	n = read();
	for(int i = 1; i <= n; i++) q[i].l = read(), q[i].r = read(), q[i].x = read(), st.insert(q[i].l), st.insert(q[i].r);
	
	sort(q + 1, q + 1 + n);
	
	for(set<int>::iterator it = st.begin(); it != st.end(); it++) {
		dfn[*it] = ++tot; raw[tot] = (*it);//这里是离散化 
	}
	raw[tot + 1] = raw[tot] + 1;//最后最好加一个点 
	
	for(int i = 1; i <= n; i++) {
		change(1, 1, tot, dfn[q[i].l], dfn[q[i].r], q[i].x);//操作 
	}
	
	ask(1, 1, tot);
	printf("%lld\n", ans);
	return 0;
}