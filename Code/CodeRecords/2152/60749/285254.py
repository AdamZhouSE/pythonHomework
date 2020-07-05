#include <stack>
#include <cstdio>
using namespace std;
#define MAXN 200001
stack < int > q;
int n, cnt;
int orz[MAXN], f[MAXN];
int scc[MAXN], ans[MAXN];
bool in_queue[MAXN];

void tarjan ( int u ) {
	if ( scc[u] )
		return;
	if ( in_queue[u] ) {
		cnt ++;
		int head;
		while ( ! q.empty() && q.top() != u ) {
			head = q.top();
			scc[head] = cnt;
			ans[cnt] += orz[head];
			q.pop();
		}
		head = q.top();
		scc[head] = cnt;
		ans[cnt] += orz[head];
		q.pop();
		while ( ! q.empty() )
			q.pop();
		return;
	}
	in_queue[u] = 1;
	q.push ( u );
	tarjan ( f[u] );
	in_queue[u] = 0;
}

int dfs ( int u ) {
	if ( ans[scc[u]] )
		return ans[scc[u]];
	return ans[scc[u]] = dfs ( f[u] ) + orz[u];
}

int main() {
	scanf ( "%d", &n );
	for ( int i = 1;i <= n;i ++ )
		scanf ( "%d", &orz[i] );
	for ( int i = 1;i <= n;i ++ )
		scanf ( "%d", &f[i] );
	for ( int i = 1;i <= n;i ++ ) {
		if ( ! scc[i] ) 
			tarjan ( i );
		if ( ! scc[i] )
			scc[i] = ++ cnt;
	}
	for ( int i = 1;i <= n;i ++ )
		if ( f[i] == i )
			printf ( "%d\n", orz[i] );
		else
			printf ( "%d\n", dfs ( i ) );
	return 0;
}
