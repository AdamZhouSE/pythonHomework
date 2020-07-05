
#include<cstdio>

#include<iostream>

#include<algorithm>

#include<cstring>

#include<cmath>

using namespace std;

struct edge

{

	int next;

	int to;

}e[10000];

int dp[10000][2];

int ha[10000];

int in[10000];

int head[10000];

int cnt;

void insert(int u,int v)

{

	e[++cnt].next=head[u];

	head[u]=cnt;

	e[cnt].to=v;

	in[v]++;

}

int dfs(int now,bool flag)

{

	if(!head[now]){

		if(flag) return ha[now];

		else return 0;

	}

	for(int i=head[now];i;i=e[i].next) dp[now][flag]+=dfs(e[i].to,!flag);

	return dp[now][flag];

}

int main()

{

	int n,x,y,root;

	cin>>n;

	for(int i=1;i<=n;i++) scanf("%d",&ha[i]);

	for(int i=1;i<=n;i++) dp[i][1]=max(ha[i],0);

	for(int i=1;i<n;i++){

		scanf("%d%d",&x,&y);

		insert(y,x);

	}

	scanf("%d%d",&x,&y);

	for(int i=1;i<=n;i++){

		if(!in[i]){

			root=i;

			break;

		} 

	}

	dfs(root,0);

	dfs(root,1);

	cout<<max(dp[root][0],dp[root][1]);

	

	return 0;

}
