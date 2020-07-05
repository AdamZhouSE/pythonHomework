#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n,ans,cnt;
int gcd(int a,int b)
{
	if(b==0) return a;
	cnt+=a/b;
	return gcd(b,a%b);
}
int main()
{
	scanf("%d",&n);
	ans=1<<29;
	for(int i=1; i<=n; i++)
	{
		cnt=0;
		if(gcd(n,i)==1)
			ans=min(ans,cnt-1);
	}
	printf("%d",ans);
	return 0;
}