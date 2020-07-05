#pragma GCC optimize(3)
#include<bits/stdc++.h>
#define il inline
#define rg register
#define gi read<int>
using namespace std;
const int N = 2e4 + 10, K = 5e4 + 10;
typedef long long ll;
struct LL{
	int l, r, v;
	il bool operator < (LL rhs) {
		return r - l < rhs.r - rhs.l;
	}
}s[K];
template<class TT>
il TT read() {
	TT o = 0, fl = 1; char ch = getchar();
	while (!isdigit(ch)) fl ^= ch == '-', ch = getchar();
	while (isdigit(ch)) o = o * 10 + ch - '0', ch = getchar();
 	return fl ? o : -o;
}
int kk, k, n, c, ans, bus[N];
int main() {
	kk = gi(), n = gi(), c = gi();
	for (int i = 1; i <= kk; ++i){
		int L = gi(), R = gi(), V = gi();
		if (V > c) V = c;
		s[++k] = (LL){L, R, V};
	}
	sort(s + 1, s + k + 1);
	for (int i = 1; i <= k; ++i) {
		int minn = s[i].v;
		for (int j = s[i].l; j < s[i].r; ++j) {
			minn = min(minn, c - bus[j]);
			if (!minn) break;
		}
		if (!minn) continue;
		ans += minn;
		for (int j = s[i].l; j < s[i].r; ++j)
			bus[j] += minn;
	}
	printf("%d\n", ans);
	return 0;
}