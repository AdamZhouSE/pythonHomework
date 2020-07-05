#include<iostream>
#include<cstdio>
using namespace std;

int n,a[40],root[40][40];
long long dp[40][40];

long long dfs(int L,int R){
	if(L>R) return 1;       //因为要左右子节点相乘，所以如果是空则给1 
	
	if(dp[L][R]) return dp[L][R];  //关键一步，记忆化，以前走过那就直接返回结果 
	
	long long maxn = 0;
	for(int i=L;i<R;i++){
		long long t = dfs(L,i-1) * dfs(i+1,R) + a[i];
		if(t > maxn){
			maxn = t;
			root[L][R] = i;
		}
	}
	return dp[L][R] = maxn;	
}	


void dg(int L,int R){
	if(L>R) return ;            //防止出现 L >R 
	printf("%d ",root[L][R]);
	dg(L,root[L][R]-1);
	dg(root[L][R]+1,R);
}

int main(){
	
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
		dp[i][i] = a[i];
		root[i][i] = i;
	}
	printf("%lld\n",dfs(1,n));
	dg(1,n);
	
	return 0;
} 
