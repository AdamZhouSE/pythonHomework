#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<bitset>
#include<ctime>
#include<deque>
#include<stack>
#include<functional>
#include<sstream>
//#include<cctype>
//#pragma GCC optimize(2)
using namespace std;
#define maxn 900005
#define inf 0x7fffffff
//#define INF 1e18
#define rdint(x) scanf("%d",&x)
#define rdllt(x) scanf("%lld",&x)
#define rdult(x) scanf("%lu",&x)
#define rdlf(x) scanf("%lf",&x)
#define rdstr(x) scanf("%s",x)
typedef long long  ll;
typedef unsigned long long ull;
typedef unsigned int U;
#define ms(x) memset((x),0,sizeof(x))
const long long int mod = 1e9 + 7;
#define Mod 1000000000
#define sq(x) (x)*(x)
#define eps 1e-3
typedef pair<int, int> pii;
#define pi acos(-1.0)
//const int N = 1005;
#define REP(i,n) for(int i=0;i<(n);i++)
typedef pair<int, int> pii;
inline ll rd() {
	ll x = 0;
	char c = getchar();
	bool f = false;
	while (!isdigit(c)) {
		if (c == '-') f = true;
		c = getchar();
	}
	while (isdigit(c)) {
		x = (x << 1) + (x << 3) + (c ^ 48);
		c = getchar();
	}
	return f ? -x : x;
}
 
ll gcd(ll a, ll b) {
	return b == 0 ? a : gcd(b, a%b);
}
int sqr(int x) { return x * x; }
 
 
/*ll ans;
ll exgcd(ll a, ll b, ll &x, ll &y) {
	if (!b) {
		x = 1; y = 0; return a;
	}
	ans = exgcd(b, a%b, x, y);
	ll t = x; x = y; y = t - a / b * y;
	return ans;
}
*/
int n, m;
struct node {
	int l, r;
	int sum;
	int lazy;
}tree[maxn];
void pushup(int rt) {
	tree[rt].sum = tree[rt << 1].sum | tree[rt << 1 | 1].sum;
}
void pushdown(int rt) {
	if (tree[rt].lazy) {
		tree[rt << 1].lazy = tree[rt].lazy;
		tree[rt << 1 | 1].lazy = tree[rt].lazy;
		tree[rt << 1].sum = tree[rt].lazy;
		tree[rt << 1 | 1].sum = tree[rt].lazy;
		tree[rt].lazy = 0;
	}
}
void build(int l, int r, int rt) {
	tree[rt].l = l; tree[rt].r = r; tree[rt].lazy = 0;
	if (l == r) {
		tree[rt].sum = 1; return;
	}
	int mid = (l + r) >> 1;
	build(l, mid, rt << 1); build(mid + 1, r, rt << 1 | 1);
	pushup(rt);
}
 
void upd(int col, int L, int R, int l, int r,int rt) {
	if (L <= l && r <= R) {
		tree[rt].sum = (1 << (col - 1));
		tree[rt].lazy = (1 << (col - 1));
		return;
	}
	pushdown(rt);
	int mid = (l + r) >> 1;
	if (L <= mid)upd(col, L, R, l, mid, rt << 1);
	if (mid < R)upd(col, L, R, mid + 1, r, rt << 1 | 1);
	pushup(rt);
}
int query(int L, int R, int l, int r, int rt) {
	if (L <= l && r <= R) {
		return tree[rt].sum;
	}
	pushdown(rt);
	int mid = (l + r) >> 1;
	int ans = 0;
	if (L <= mid)ans |= query(L, R, l, mid, rt << 1);
	if (mid < R)ans |= query(L, R, mid + 1, r, rt << 1 | 1);
	return ans;
}
 
int main() {
	//ios::sync_with_stdio(0);
	rdint(n); int T; rdint(T); rdint(m);
	build(1, n, 1);
	while (m--) {
		char op; cin >> op;
		if (op == 'C') {
			int a, b, c; rdint(a); rdint(b); rdint(c);
			if (a > b)swap(a, b);
			upd(c, a, b, 1, n, 1);
		}
		else {
			int a, b; rdint(a); rdint(b);
			if (a > b)swap(a, b);
			int tot = 0;
			int ans = query(a, b, 1, n, 1);
			for (int i = 1; i <= T; i++) {
				if (ans&(1 << (i - 1))) {
					tot++;
				}
			}
			cout << tot << endl;
		}
	}
	return 0;
}