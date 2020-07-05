#include <bits/stdc++.h>

using namespace std;
const int N = 3e5 + 10;
typedef long long ll;

struct Node{
	int maxn , tg;
}tr[N*4];

void down(int o)
{
	if (tr[o].tg)
	{
		tr[o<<1].maxn += tr[o].tg;
		tr[o<<1].tg += tr[o].tg;
		
		tr[o<<1|1].maxn += tr[o].tg;
		tr[o<<1|1].tg += tr[o].tg;	
		
		tr[o].tg = 0;
	}
}

void up(int o){
	tr[o].maxn = max(tr[o<<1].maxn , tr[o<<1|1].maxn);
}
void modify(int o,int l,int r,int ql,int qr,int val)
{
	if (ql <= l && r <= qr)
	{
		tr[o].tg += val;
		tr[o].maxn += val;
		return ;
	}	
	int mid = l + r >> 1;
	down(o);
	if (ql <= mid) modify(o<<1,l,mid,ql,qr,val);
	if (mid < qr ) modify(o<<1|1,mid+1,r,ql,qr,val);
	up(o);
}

int n , cnt , h[N];
int maxn[N] , minm[N];
int isl[N] , isr[N];
int L[N] , R[N];
ll ans;
vector <int> l , r;
vector <int> posl , posr;
vector <int> ::iterator it;

struct Line{
	int y;
	int lx , rx , val;
	inline bool operator < (const Line &a) const{
		return y < a.y;
	}
}ln[2*N];int lcnt;


struct BinaryIndexedTree {
	int X[N];
	#define Lowbit(a) (a&(-a))
	
	void mdy(int pos) {while(pos<=n) {++X[pos];pos+=Lowbit(pos);}}
	int qry(int pos) {
		int sum = 0;
		while(pos) {sum += X[pos];pos-=Lowbit(pos);}
		return sum;
	}
}bt;
ll GetReverseNumber() {
	ll ans = 0;
	for(int i = 1; i <= n ; ++i) {
		ans += bt.qry(n) - bt.qry(h[i]);
		bt.mdy(h[i]);
	}
	return ans;
}
ll reversal;
int a[N] , b[N];
int main()
{
	scanf("%d",&n);
	for (int i = 1;i <= n;i++) scanf("%d",&h[i]) , a[i] = h[i];
	
	sort(a + 1 , a + 1 + n);
	cnt = unique(a + 1 , a + 1 + n) - a - 1;
	for (int i = 1;i <= n;i++) h[i] = lower_bound(a + 1 , a + 1 + cnt , h[i]) - a;
	reversal = GetReverseNumber();
	if (!reversal) {
		return cnt == n ? puts("1") : puts("0") , 0;
	}
	for (int i = 1;i <= n;i++)
	{
		maxn[i] = h[i];
		if (i ^ 1) maxn[i] = max(maxn[i] , maxn[i-1]);
		if (maxn[i] == h[i] && maxn[i - 1] != h[i]) 
		{
			isl[i] = true;
			
			l.push_back(h[i]);
			posl.push_back(i);
		}
	}
	
	
	for (int i = n;i >= 1;i--)
	{
		minm[i] = h[i];
		if (i ^ n) minm[i] = min(minm[i] , minm[i+1]);
		if (minm[i] == h[i] && minm[i + 1] != h[i]) 
		{
			isr[i] = true;
			r.push_back(h[i]);
			posr.push_back(i);
		}
	}

	memset(L , -1 , sizeof L);
	memset(R , -1 , sizeof R);
	reverse(r.begin(),r.end());
	reverse(posr.begin(),posr.end());
	for (int i = 1;i <= n;i++)
	{
		it = upper_bound(l.begin() , l.end() , h[i]);
		if (it != l.end()){
			L[i] = posl[it-l.begin()];
		}
		
		it = lower_bound(r.begin() , r.end() , h[i]);
		if (it != r.begin()){
			it--;R[i] = posr[it-r.begin()];
		}
		
		if (~L[i] && ~R[i]){
			if (L[i] <= i - 1 && i + 1 <= R[i]){
				ln[++lcnt] = (Line) {i + 1 , L[i] , i - 1 , 2};
				ln[++lcnt] = (Line) {R[i] + 1 , L[i] , i - 1 , -2};
			}
			
		}	
		
		it = lower_bound(l.begin() , l.end() , h[i]);
		
		if (*it == h[i] && !isl[i]){
			if (~R[i]){
				int pos = posl[it-l.begin()];
				ln[++lcnt] = (Line) {i + 1 , pos , pos , 1};
				ln[++lcnt] = (Line) {R[i] + 1 , pos , pos , -1};
			
			}
		}
		
		it = lower_bound(r.begin() , r.end() , h[i]);
		
		if (*it == h[i] && !isr[i]){
			if (~L[i]){
				int pos = posr[it-r.begin()];
				ln[++lcnt] = (Line) {pos , L[i] , i - 1 , 1};
				ln[++lcnt] = (Line) {pos + 1 , L[i] , i - 1 , -1};
		
			}
		}
		
	}
	
	
		
	sort(ln + 1 , ln + 1 + lcnt);
	for (int i = 1;i <= lcnt;i++)
	{
		int j = i;
		while (j <= lcnt && ln[j].y == ln[i].y)
		{
			modify(1 , 1 , n , ln[j].lx , ln[j].rx , ln[j].val);
			j++;
		}
		i = j - 1;
		ans = max(ans , 1ll * tr[1].maxn );
	}
	cout<<reversal - ans - 1<<endl;
	return 0;
}