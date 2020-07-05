#include<cstdio>
#include<iostream> 
#include<cstdlib>
#include<cmath>
#include<cstring>
using namespace std;
int a,b,c,i,j,k,l,m,n,inf=9999999,sum,max1;
int e[101][101],minn[101];
bool u[101];
int main()
{
    cin>>n>>m;
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    if(i==j)
    e[i][j]=0;
    else
    e[i][j]=inf;//构造邻接矩阵 
    for(i=1;i<=m;i++)
    {
        cin>>a>>b>>c;
        e[a][b]=e[b][a]=c;
        max1+=c;//max储存所有的畅通程度 
}//读入数据并存入矩阵
    memset(minn,0x7f,sizeof(minn));
    minn[1]=0;    
    memset(u,1,sizeof(u));//初始化为True，表示所有点未被访问 
    for(i=1;i<=n;i++)
    {
        k=0;
        for(j=1;j<=n;j++)//寻找一个与已访问的点相连的权值最小的未被访问的点k 
        if(u[j] && minn[j]<minn[k])
        k=j;
        u[k]=false;//将k加入最小生成树，标记已访问 
        for(j=1;j<=n;j++)//修改与k相连的所有未被访问的点 
        if(u[j] && e[k][j]<minn[j])
        minn[j]=e[k][j];
    }
    for(i=1;i<=n;i++)
    sum+=minn[i];//累加权值 
    cout<<max1-sum;
    return 0;
}
