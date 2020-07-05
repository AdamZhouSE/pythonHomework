#include<bits/stdc++.h>
using namespace std;
const int M=105;
char ch[M];
int dp[M][M];
bool merge(int l1,int r1,int l2,int r2)
{
	if((r1-l1+1)%(r2-l2+1))return 0;
	for(int i=l1;i<=r1;++i)if(ch[i]!=ch[(i-l1)%(r2-l2+1)+l2])return 0;
	return 1;
}
int lg(int x){int t=0;while(x){x/=10;t++;}return t;}
int dfs(int l,int r)
{
	if(l==r)return 1;
	if(dp[l][r])return dp[l][r];
	int ans=r-l+1;
	for(int i=l;i<r;++i)
	{
		ans=min(ans,dfs(l,i)+dfs(i+1,r));
		if(merge(i+1,r,l,i))ans=min(ans,dfs(l,i)+2+lg((r-i)/(i-l+1)+1));
	}
	return dp[l][r]=ans;
}
void in(){scanf("%s",ch+1);}
void ac(){printf("%d\n",dfs(1,strlen(ch+1)));}
int main(){in(),ac();}