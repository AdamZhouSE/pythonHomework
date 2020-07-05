#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

int pre[100005];

int find(int x)
{
	if(x==pre[x])
	{
		return x;
	}
	else
	{
		return pre[x]=find(pre[x]);
	}
}
int a[100005];
bool merge(int x,int y)
{
	int fx=find(x);
	int fy=find(y);
	if(fx!=fy)
	{
		if(a[fx]>=a[fy])
		pre[fx]=fy;
		else
		{
			pre[fy]=fx;
		}
		
		return true;
	} 
	else
	{
		return false;
	}
}
int main()
{
	int n,m;
	cin>>n>>m;
	for(int i=1;i<=n;i++)
	pre[i]=i;
	for(int i=1;i<=n;i++)
	scanf("%d",&a[i]);
	int x,y;
	long long int sum=0;
    for(int i=1;i<=m;i++)
    {
      scanf("%d%d",&x,&y);
	  if(merge(x,y)==true)
	  {
	    merge(x,y);	
	  }	
	}

	for(int i=1;i<=n;i++)
	{
		if(find(i)==i)
		{
			sum+=a[i];
		}
	}
	
	cout<<sum<<endl;
	
	return 0;
}