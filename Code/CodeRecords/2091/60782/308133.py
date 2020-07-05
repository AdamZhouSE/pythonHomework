#include<bits/stdc++.h>
using namespace std;

vector<int>link[1066];
int n,m;
int linker[1066];
bool vis[1066];

bool dfs(int x)
{
	//printf("__ %d\n",x);
	for(auto y:link[x])
	{
		if(!vis[y])
		{
			vis[y]=1;
			if(linker[y]==-1||dfs(linker[y]))
			{
				linker[y]=x;
				return true;
			}
		}
	}return false;
}

int main()
{
	scanf("%d%d",&n,&m);
	for(int i=0;i<m;i++)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		link[i].push_back(x);
		link[i].push_back(y);
	}
	for(int i=0;i<n;i++)linker[i]=-1;
	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)vis[j]=0;
		if(!dfs(i))
		{
			printf("%d\n",i);
			return 0;
		}
	}
	printf("%d\n",m);
	return 0;
}