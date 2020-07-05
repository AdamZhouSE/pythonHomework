
#include<bits/stdc++.h>
using namespace std;
int k,m;
int v[10000000];
int ans[10000];
int dfs(int num,int deep)
{
	if (v[num]==1) return 0;//若当前数被枚举到
	if (deep==m) return 1;
	v[num]=1;
	ans[deep]=num & 1; 
	if (dfs((num<<1)&(m-1),deep+1)) return 1;
	if (dfs((num<<1|1)&(m-1),deep+1)) return 1;
	v[num]=0;
	return 0;
}
int main(void)
{
	cin>>k;
	m=1<<k;
	cout<<m<<' ';
	dfs(0,1);	
	for (int i=1;i<k;++i) cout<<0;
	for (int i=1;i<=m-k+1;++i) cout<<ans[i];
    cout<<endl;
	return 0;
} 
