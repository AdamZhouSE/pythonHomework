#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 200005;
const int maxt = 7500000;
int n;
int a[maxn];
int read()
{
	char ch = getchar(); bool f = 1;
	while(ch < '0' || ch > '9') f &= ch != '-' , ch = getchar();
	int res = 0;
	while(ch >= '0' && ch <= '9') res = (res << 3) + (res << 1) + (ch ^ 48) , ch = getchar();
	return f ? res : -res;
}
void write(int x)
{
	if(x < 0) x = -x , putchar('-');
	int len = 0 , res[15];
	for(;x;res[++len] = x % 10 , x /= 10);
	for(int i = len;i >= 1;i--) putchar(res[i] + 48);
	if(!len) putchar('0');
}
struct inm{int ls , rs , cnt;};
struct CT
{
	private:
		int m;
		int b[maxn];
		int cnt;
		inm t[maxt]; int rt[maxn];
		void build(int &p , int l , int r)
		{
			p = ++cnt;
			if(l == r) return;
			int mid = l + r >> 1;
			build(t[p].ls , l , mid);
			build(t[p].rs , mid + 1 , r);
		}
		void update(int &p , int pre , int l , int r , int x)
		{
			p = ++cnt;
			t[p] = t[pre];
			t[p].cnt++;
			if(l == r) return;
			int mid = l + r >> 1;
			if(x <= mid) update(t[p].ls , t[pre].ls , l , mid , x);
			else update(t[p].rs , t[pre].rs , mid + 1 , r , x);
		}
		int kth(int p , int pre , int l , int r , int k)
		{
			if(l == r) return l;
			int mid = l + r >> 1 , num = t[t[p].ls].cnt - t[t[pre].ls].cnt;
			if(num >= k) return kth(t[p].ls , t[pre].ls , l , mid , k);
			else return kth(t[p].rs , t[pre].rs , mid + 1 , r , k - num);
		}
	public:
		void clear()
		{
			cnt = 0;
			for(int i = 1;i <= n;i++) rt[i] = 0;
		}
		void init()
		{
			for(int i = 1;i <= n;i++) b[i] = a[i];
			sort(b + 1 , b + n + 1);
			m = unique(b + 1 , b + n + 1) - b - 1;
			build(rt[0] , 1 , m);
			for(int i = 1;i <= n;i++)
			{
				int loc = lower_bound(b + 1 , b + m + 1 , a[i]) - b;
				update(rt[i] , rt[i - 1] , 1 , m , loc);
			}
		}
		int query(int l , int r , int k){return b[kth(rt[r] , rt[l - 1] , 1 , m , k)];}
}ct;
int main()
{
	n = read();
	int q = read();
	for(int i = 1;i <= n;i++) a[i] = read();
	ct.clear() , ct.init();
	while(q--)
	{
		int l = read() , r = read() , k = read();
		write(ct.query(l , r , k));
		putchar('\n');
	}
	return 0;
}