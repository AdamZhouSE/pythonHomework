#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
typedef long long ll;
const int maxn = 500000 + 10;
//const int maxn = 100 + 10;
const int maxt = 1500000 + 10;
const int MOD = 1000000007;
const int DEBUG = 0;

inline int inc(int a, int b) { return (a + b >= MOD) ? (a + b - MOD) : (a + b); }
inline int dec(int a, int b) { return (a >= b) ? (a - b) : (a + MOD - b); }
inline int mul(int a, int b) { return 1LL * a * b % MOD; }

inline int power(int x, int k) {
	int tmp = 1;
	while(k) {
		if(k & 1) tmp = mul(tmp,x);
		x = mul(x,x);
		k >>= 1;
	}
	return tmp;
}

char s[maxn];
int ln;

//SA

int sa[maxn], rk[2][maxn], tim, Log[maxn];
int h1[maxn], f1[21][maxn];
int h2[maxn], f2[21][maxn];

inline int query1(int l, int r) {
	l ++; int k = Log[r - l + 1];
	return min(f1[k][l],f1[k][r - (1 << k) + 1]);
}

inline int query2(int l, int r) {
	l ++; int k = Log[r - l + 1];
	return min(f2[k][l],f2[k][r - (1 << k) + 1]);
} 

inline int LCP(int x, int y) {
	int l = min(rk[0][x],rk[0][y]), r = max(rk[0][x],rk[0][y]);
	return query1(l,r);
}

inline int LCS(int x, int y) {
	x = ln - x + 1, y = ln - y + 1;
	int l = min(rk[1][x],rk[1][y]), r = max(rk[1][x],rk[1][y]);
	return query2(l,r);
}

//SAM
int ID;
int trans[maxt][27];
namespace SAM{
	
struct tnode{
	int len, par, ch[27], id;
	tnode() {}
	tnode(int _len, int _par):len(_len), par(_par) { id = 0; memset(ch,0,sizeof(ch)); }
}t[maxt];
int tcnt, rt, lst, val[maxn], tg[maxt];
	
inline void init() {
	memset(trans,0,sizeof(trans));
	memset(tg,0,sizeof(tg));
	tcnt = rt = lst = 1;
	t[1] = tnode(0,0);
}

inline void extend(int x, int id) {
	int p = lst, np = ++ tcnt; val[id] = x; tg[np] = 1;
	t[np] = tnode(t[p].len + 1,0); t[np].id = id;
	for(;p && !t[p].ch[x];p = t[p].par) t[p].ch[x] = np;
	if(!p) t[np].par = rt;
	else {
		int q = t[p].ch[x];
		if(t[q].len == t[p].len + 1) t[np].par = q;
		else {
			int nq = ++ tcnt; t[nq] = t[q];
			t[nq].len = t[p].len + 1;
			t[q].par = t[np].par = nq;
			for(;p && t[p].ch[x] == q;p = t[p].par) t[p].ch[x] = nq;
		}
	}
	lst = np;
}

inline void Ins(char *s, int ln) {
	for(int i = 1;i <= ln;i ++) {
		extend(s[i] - 'a',i);
	}
}

int sum[maxn], lis[maxt];
inline void build() {
	memset(sum,0,sizeof(sum));
	int Mx = 0;
	for(int i = 1;i <= tcnt;i ++) sum[t[i].len] ++, Mx = max(Mx,t[i].len);
	for(int i = 1;i <= Mx;i ++) sum[i] += sum[i - 1];
	for(int i = tcnt;i >= 1;i --) lis[sum[t[i].len] --] = i;
	
	for(int i = tcnt;i >= 1;i --) {
		int u = lis[i], pre = t[u].par;
		trans[pre][val[t[u].id - t[pre].len]] = u;
	}
	//debug
//	puts("trans");
//	for(int i = 1;i <= tcnt;i ++) {
//		printf("%d\n", i);
//		for(int j = 0;j < 26;j ++) {
//			if(!trans[i][j]) continue;
//			printf("%c %d\n", char('a' + j), trans[i][j]);
//		}
//		puts("");
//	}
}

void dfs(int u) {
	if(tg[u] && t[u].id) {
		tim ++; 
		rk[ID][ln - t[u].id + 1] = tim;
		sa[tim] = ln - t[u].id + 1;
	}
	for(int i = 0;i < 26;i ++) {
		if(trans[u][i]) dfs(trans[u][i]);
	}
}
	
}

inline void get_height(int *h, int n) {
  int k=0;
  SAM::val[0] = SAM::val[n + 1] = -1;
  reverse(SAM::val + 1,SAM::val + n + 1);
  for(int i = 1;i <= n;i ++) {
    for (int j = sa[rk[ID][i] - 1];i + k <= n && j + k <= n && SAM::val[i + k] == SAM::val[j + k];k ++);
    h[rk[ID][i]] = k; 
		if(k) k--;
  }
  reverse(SAM::val + 1,SAM::val + n + 1);
}

int c0[maxn], c1[maxn], c2[maxn];

inline void add(int l, int r, int x2, int x1, int x0) {
	if(l > r) return;
	if(DEBUG) printf("%d %d %d %d %d\n", l, r, x2, x1, x0);
	c0[l] = inc(c0[l],x0); c0[r + 1] = dec(c0[r + 1],x0);
	c1[l] = inc(c1[l],x1); c1[r + 1] = dec(c1[r + 1],x1);
	c2[l] = inc(c2[l],x2); c2[r + 1] = dec(c2[r + 1],x2);
}

inline void solve() {
	scanf("%s", s + 1);
	ln = strlen(s + 1);
	reverse(s + 1,s + ln + 1);
	ID = 0;
	SAM::init();
	SAM::Ins(s,ln);
	SAM::build();
	tim = 0;
//	cout << SAM::tcnt << endl;
	SAM::dfs(SAM::rt);
	get_height(h1,ln);
	for(int i = 1;i <= ln;i ++) f1[0][i] = h1[i];
	for(int j = 1;j <= 20;j ++) {
		for(int i = 1;i <= ln - (1 << j) + 1;i ++) f1[j][i] = min(f1[j - 1][i],f1[j - 1][i + (1 << (j - 1))]);
	}
	
	for(int i = 1, j = ln;i < j;i ++, j --) swap(s[i],s[j]);
	ID = 1;
	SAM::init();
	SAM::Ins(s,ln);
	SAM::build();
	tim = 0;
	SAM::dfs(SAM::rt);
	get_height(h2,ln);
	for(int i = 1;i <= ln;i ++) f2[0][i] = h2[i];
	for(int j = 1;j <= 20;j ++) {
		for(int i = 1;i <= ln - (1 << j) + 1;i ++) f2[j][i] = min(f2[j - 1][i],f2[j - 1][i + (1 << (j - 1))]);
	}
	
	memset(c0,0,sizeof(c0));
	memset(c1,0,sizeof(c1));
	memset(c2,0,sizeof(c2));
	int inv2 = power(2,MOD - 2);
	for(int k = 1;k <= (ln >> 1);k ++) {
		for(int i = k, j = i + k;i <= ln && j <= ln;i += k, j += k) {
			int y = LCP(i,j), x = LCS(i,j);
			if(s[i] != s[j] || x + y < k) continue;
			if(DEBUG) printf("solve: %d %d %d\n", i, j, k);
			if(DEBUG) printf("LCP: %d LCS: %d\n", y, x);
			//debug LCP
//			printf("%d %d %d\n", i, j, x);		
			int l = max(j - x + 1,i + 1), r = j + y - 1;
			if(r <= k + j) {
				int a = dec(1,inc(l,k)), b = dec(inc(2,k),l);
				add(l + k,r,inv2,mul(inv2,inc(a,b)),mul(inv2,mul(a,b)));
			}
			else {
				int a = dec(1,inc(l,k)), b = dec(inc(2,k),l);
				add(l + k,j + k,inv2,mul(inv2,inc(a,b)),mul(inv2,mul(a,b)));
				a = dec(2,inc(j,l)); b = inc(dec(j,l),1);
				add(j + k + 1,r,0,b,mul(inv2,mul(a,b)));
			}
		}
	}
	int n = ln;
	for(int i = 1;i <= n;i ++) c0[i] = inc(c0[i - 1],c0[i]);
	for(int i = 1;i <= n;i ++) c1[i] = inc(c1[i - 1],c1[i]);
	for(int i = 1;i <= n;i ++) c2[i] = inc(c2[i - 1],c2[i]);
	int Ans = 0;
	for(int i = 1;i <= n;i ++) {
    int now = 0;
		now = inc(now,mul(c2[i],mul(i,i)));
		now = inc(now,mul(c1[i],i));
		now = inc(now,c0[i]);
		Ans = inc(Ans,now);
		printf("%d\n", Ans);
	}
}

int main() {
//	freopen("data2.in","r",stdin);
	Log[0] = Log[1] = 0;
	for(int i = 2;i <= 500000;i ++) Log[i] = Log[i >> 1] + 1;
	solve();
	return 0;
}