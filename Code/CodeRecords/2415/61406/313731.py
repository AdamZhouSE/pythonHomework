#include<bits/stdc++.h>
#define LL long long
#define pa pair<int,int>
#define ls k<<1
#define rs k<<1|1
#define inf 0x3f3f3f3f
using namespace std;
const int N=100010;
const int M=2000100;
const LL mod=1000007;
int n,w[100],root[100][100];
LL dp[100][100];
LL dfs1(int l,int r){
	if(l>r) return 1ll; 
	if(dp[l][r]!=-1) return dp[l][r];
	LL mmax=0;
	for(int k=l;k<=r;k++){
		LL sum=dfs1(l,k-1)*dfs1(k+1,r)+w[k];
		if(sum>mmax){
			root[l][r]=k;
			mmax=sum;
		}
	}
	return dp[l][r]=mmax;
}
void dfs2(int l,int r){
	if(l>r) return;
	int rt=root[l][r];
	cout<<rt<<" ";
	dfs2(l,rt-1);
	dfs2(rt+1,r);
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>w[i];
	memset(dp,-1,sizeof(dp));
	for(int i=1;i<=n;i++) dp[i][i]=w[i],root[i][i]=i;
	cout<<dfs1(1,n)<<endl;
	dfs2(1,n);
	return 0;
}
