#include<bits/stdc++.h>
using namespace std;
const int MAXN = 1e3 + 5;
int n, a[MAXN];
int main()
{
	while(~scanf("%d", &n))
	{
		for(int i = 0; i < n; i++) scanf("%d", &a[i]);
		int ans = 0;
		for(int i = 1; i < n - 1; i++)
		{
			if(a[i] < a[i - 1] && a[i] < a[i + 1] ||
			   a[i] > a[i - 1] && a[i] > a[i + 1])
				ans++;
		}
		printf("%d\n",ans);
	}
    return 0;
}