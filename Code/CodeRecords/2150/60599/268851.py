
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m,q,ans,F[21][1025][1025],dist[21][21],s[11],t[11],l[11],r[11];
void Update(int k)
{
	int tot=0;
	for(int ta=1;ta<=q;ta++)
		if(!(k&(1<<ta-1)))
			tot++;
	if(tot>ans) ans=tot;
}
void DFS(int i,int j,int k)
{
	Update(k);//更新答案
	for(int ta=1;ta<=q;ta++)
	{
		if(k&(1<<ta-1))//第ta个任务未派送
		{
			if(j&(1<<ta-1))//身上已经带了第ta个任务,把任务送达
			{
				if(F[i][j][k]+dist[i][t[ta]]<F[t[ta]][j-(1<<ta-1)][k-(1<<ta-1)]&&F[i][j][k]+dist[i][t[ta]]<=r[ta])
				{
					F[t[ta]][j-(1<<ta-1)][k-(1<<ta-1)]=F[i][j][k]+dist[i][t[ta]];
					DFS(t[ta],j-(1<<ta-1),k-(1<<ta-1));
				}
			}
			else//身上没有第ta个任务，去把任务取来
			{
				if(max(F[i][j][k]+dist[i][s[ta]],l[ta])<F[s[ta]][j+(1<<ta-1)][k])
				{
					F[s[ta]][j+(1<<ta-1)][k]=max(F[i][j][k]+dist[i][s[ta]],l[ta]);
					DFS(s[ta],j+(1<<ta-1),k);
				}
			}
		}
	}
}
int main()
{
	scanf("%d%d%d",&n,&m,&q);
	memset(dist,63,sizeof(dist));memset(F,63,sizeof(F));
	for(int i=1;i<=m;i++)
	{
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		if(dist[a][b]>c) dist[a][b]=c;
	}
	for(int i=1;i<=q;i++)
		scanf("%d%d%d%d",&s[i],&t[i],&l[i],&r[i]);
	for(int k=1;k<=n;k++)                            //Floyd刷出每两点间的最短路
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				if(dist[i][k]+dist[k][j]<dist[i][j])
					dist[i][j]=dist[i][k]+dist[k][j];
	for(int i=1;i<=n;i++) dist[i][i]=0;
	F[1][0][(1<<q)-1]=0;
	DFS(1,0,(1<<q)-1);
	printf("%d",ans);
	return 0;
}