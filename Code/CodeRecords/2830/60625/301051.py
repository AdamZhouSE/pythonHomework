#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<cctype>
using namespace std;

#define PI acos(-1.0)
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;	
const int INF32M=0x3f3f3f3f;
const ll INF64M=0x3f3f3f3f3f3f3f3f;
const int maxn=1e5+5;
int a[100005];	//k个系数 
int main()
{
	ios::sync_with_stdio(false);
	int b,k,cnt=0;
	cin>>b>>k;
	for(int i=1;i<=k;i++)
		cin>>a[i];
	if(b%2==0)
	{
		if(a[k]%2==0)	//ak为偶数 
			cout<<"even"<<endl;
		else	//偶+奇=奇 
			cout<<"odd"<<endl;
	}
	else	//底数b为奇数 
	{
		for(int i=1;i<=k;i++)
		{
			if(a[i]%2!=0)	//奇*奇=奇 
				cnt++;
			//else 奇(b^k)*偶(系数)=偶 
		}
		if(cnt%2==0)	//奇系数有偶数个 奇数项就有偶数个 3+7=10
			cout<<"even"<<endl;
		else	//奇+奇=偶 奇+奇+奇=奇 
			cout<<"odd"<<endl;
	} 
	return 0;
}

