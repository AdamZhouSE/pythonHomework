#include<iostream>
using namespace std;
#define  N 3000
int e[N][N],dis[N],book[N];
int main(){
	
	int i,j,n,m,t1,t2,t3,u,v,min,s,t;
	int inf=99999999;

	cin>>n>>m>>s>>t;

//初始化
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			if(i==j) e[i][j]=0;
				else e[i][j]=inf;
		}
	}
//读入边
	for(i=1;i<=m;i++)
	{
		cin>>t1>>t2>>t3;
		e[t1][t2]=t3;
		e[t2][t1]=t3;	//去掉该向变成有向图
	}

//初始化dis数组，这里1号顶点到其余各个顶点的初始路程
	for(i=1;i<=n;i++){
		dis[i]=e[s][i];
	}
//book数组初始化
	for(i=1;i<=n;i++)
		book[i]=0;

	book[i]=1;
//Dijkstra算法核心
	for(i=1;i<=n-1;i++){
		min=inf;	//找到离1号顶点最近的顶点
		for(j=1;j<=n;j++){

			if(book[j]==0 && dis[j]<min){
				min=dis[j];
				u=j;
			}

		}
		book[u]=1;

		for(v=1;v<=n;v++){
			if(e[u][v]<inf){

				if(dis[v]>dis[u]+e[u][v])
					dis[v]=dis[u]+e[u][v];
			}
		}
	}
	//输出结果
		cout<<dis[t]<<endl;;
		
	return 0;
}

