
#include"stdio.h"

#include"stdlib.h"

#include"string.h"

#include"algorithm"

#include"vector"

#include"iostream"

using namespace std;

const int maxn=1000;

const int INF=1e9;

vector<int>G[maxn];

int son[maxn];//然后设son[i]表示以i为根的子树的节点个数(不包括根)

int ans,n,balance;

void ReadTree()

{//输入n-1条边 

	scanf("%d",&n);

	for(int i=0;i<n-1;i++)

	{

		int s,e;

		scanf("%d%d",&s,&e);

		G[s].push_back(e);

		G[e].push_back(s);

	}

}

void dfs(int v,int fa)

{//O(n)搜一遍即可 

	son[v]=0;

	int d=G[v].size();

	int pre_balance=0;

	for(int i=0;i<d;i++)

	{

		int k=G[v][i];

		if(k!=fa)

		//这里可以记忆化搜索，没必要

		//这题dfs本来就不会重复，

		//保证孩子节点跟父亲节点不等就行 

		{

			dfs(k,v);

			son[v]+=son[k]+1;//注意son[k] 不是son[i],因为这个马虎调试了很久 

			pre_balance=max(pre_balance,son[k]+1);

		} 

	}

	pre_balance=max(pre_balance,n-son[v]-1);

	//printf("删除节点： %d 最大子树节点数%d\n",v,pre_balance); 

	if(pre_balance<balance||(pre_balance==balance&&v<ans))

	{

	     //平衡的同时还要重心节点最小 

		ans=v;

		balance=pre_balance;

	    //printf("ans=%d bal=%d\n",ans,balance); 

	}

}

int main()

{

	ReadTree();

	memset(son,0,sizeof(son));

	ans=0;balance=INF;

	dfs(0,-1);

	printf("重心节点： %d\n平衡（最大子树最少节点数）： %d",ans,balance);

	return 0;

}
