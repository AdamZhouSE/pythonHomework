#include <cmath>   
#include <cstdio>  
#include <string>  
#include <cstring>  
#include <iostream>  
#include <algorithm>
using namespace std;
int hgt[1001];
int main()
{
	int n,m,cnt,ans=0;
	cin>>n>>m;
	memset(hgt,0,sizeof hgt);
	for(int i=0;i<n;i++)
	{
		cin>>hgt[i];
	}
	sort(hgt,hgt+n);
	for(int i=0;i<n;i++)
	{
		cnt=0;
		for(int j=i+1; hgt[j]<=hgt[i]+m && j<n; j++ )
		{
			cnt++;
		}
		ans+= 2*cnt;
	}
	printf("%d\n",ans);
	return 0;
}