#include <cstdio>
#include <iostream>
#include <map>
#define maxn 100010
long long ans;
namespace SAM {
#define N (maxn << 1)
#define root 1
	int R[N], fail[N];
	std::map<int, int> nxt[N];
	int lst = root, idx = root;
	void append(int ch) {
		int p = lst, np = lst = ++idx;
		R[np] = R[p] + 1;
		for (; p && !nxt[p].count(ch); p = fail[p]) nxt[p][ch] = np;
		if (!p) fail[np] = root;
		else {
			int q = nxt[p][ch];
			if (R[p] + 1 == R[q]) fail[np] = q;
			else {
				int nq = ++idx;
				nxt[nq] = nxt[q], fail[nq] = fail[q], R[nq] = R[p] + 1, fail[np] = fail[q] = nq;
				for (; p && nxt[p].count(ch) && nxt[p][ch] == q; p = fail[p]) nxt[p][ch] = nq;
			}
		}
	}
	int query() {
		return R[lst] - R[fail[lst]];
	}
#undef root
#undef N
}
 
int n;
int main() {
	std::ios::sync_with_stdio(false), std::cin.tie(0), std::cout.tie(0);
	std::cin >> n;
	for (int i = 0, x; i < n; i++) {
		std::cin >> x;
		SAM::append(x);
		std::cout << (ans += SAM::query()) << '\n';
	}
	return 0;
}