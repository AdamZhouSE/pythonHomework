
#include<bits/stdc++.h>
using namespace std;
const int MAXN=101;
 
int line[MAXN][MAXN];
int fp[MAXN],used[MAXN],m,n;
 
bool find(int x)
{
	for(int i=m+1;i<=n;++i)
	{
		if(line[x][i]&&!used[i])
		{
			used[i]=1;
			if(!fp[i]||find(fp[i]))
			{
				fp[i]=x;
				return true;
			}
		}
	}
	return false;
}
 
int main()
{
	int x,y;
	scanf("%d%d",&n,&m);
	memset(line,0,sizeof(line));
	memset(fp,0,sizeof(fp));
	while(scanf("%d%d",&x,&y)!=EOF)
	{
		line[x][y]=1;
	}
	int sum=0;
	for(int i=1;i<=m;++i)
	{
		memset(used,0,sizeof(used));
		if(find(i))
		  sum++;
	}
    cout<<sum;
	cout<<endl;
}
