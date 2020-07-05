#include<bits/stdc++.h>

using namespace std;
#define ll int
#define il inline
#define rg register
#define mp make_pair
#define rp(i,x,y) for(rg ll i=x;i<=y;++i)

ll n, cntv, cnte;
vector< pair<ll, ll> >as;

il ll read()
{
	rg char ch = getchar(); rg ll x = 0; rg bool y = 1;
	while (ch != '-' && (ch > '9' || ch < '0'))ch = getchar();
	if (ch == '-')ch = getchar(), y = 0;
	while (ch <= '9' && ch >= '0')x = (x << 3) + (x << 1) + (ch^'0'), ch = getchar();
	return y ? x : -x;
}
il ll gt(ll x) { ll tmp = sqrt(x) + 5; while (tmp*(tmp - 1) > (x << 1))--tmp; return tmp; }

int main()
{
	n = read();
	while (n)
	{
		ll tmp = (1 + sqrt(8 * n + 1)) / 2 + 1e-8;
		if (cntv)as.push_back(mp(1, cntv + tmp)), ++cnte;
		rp(i, cntv + 1, cntv + tmp - 1) { 
			as.push_back(mp(i, i + 1));
			++cnte;
			as.push_back(mp(cntv + tmp, cntv + 1));
			++cnte;
		}
		cntv += tmp;
		n -= tmp * (tmp - 1) / 2;
	}
	printf("%d %d\n", cntv, cnte);
	rp(i, 0, cnte - 1)printf("%d %d\n", as[i].first, as[i].second);
	return 0;
}
