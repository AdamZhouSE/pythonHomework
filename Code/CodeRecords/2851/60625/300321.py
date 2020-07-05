#include<bits/stdc++.h>
#define ll long long
using namespace std;
 
int main() 
{
	int n;
	cin>>n;
	ll ans = -1;
	int a,b;
	for(int i = 1; i<=n; i++) {
		scanf("%d%d",&a,&b);
		ans = max(ans,(ll)a+b);
	}
	cout << ans << endl;
	return 0;
}