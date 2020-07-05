#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int maxx=1e3+10;
struct node{
	int ping;
	int ac;
	int wa;
}p[maxx];
int n;

int main()
{
	while(scanf("%d",&n)!=EOF)
	{
		int sum1=0;
		int sum2=0;
		int sum1a=0;
		int sum1w=0;
		int sum2a=0;
		int sum2w=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d",&p[i].ping,&p[i].ac,&p[i].wa);
			if(p[i].ping==1)
			{
				sum1+=(p[i].ac+p[i].wa);
				sum1a+=p[i].ac;
				sum1w+=p[i].wa;
			}
			else
			{
				sum2+=(p[i].ac+p[i].wa);
				sum2a+=p[i].ac;
				sum2w+=p[i].wa;
			}
		}
		if(sum1a*2>=sum1) cout<<"LIVE"<<endl;
		else cout<<"DEAD"<<endl;
		if(sum2a*2>=sum2) cout<<"LIVE"<<endl;
		else cout<<"DEAD"<<endl;
	}
}