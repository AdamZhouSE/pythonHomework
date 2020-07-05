#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int n,i;
	int x[1001],y[1001];
	double tan[1001]; 
	while(scanf("%d %d %d",&n,&x[0],&y[0])!=EOF)
	{
		int z = 0;
		int flag[1001] = {0};
		for (i=1;i<=n;i++)
			scanf("%d %d",&x[i],&y[i]);
		for (i=1;i<=n;i++)
		{
			if (x[i]-x[0]==0)
				tan[i] = 1e9;//可以理解为斜率无穷大
			else
				tan[i] = (double)(y[i]-y[0])/(double)(x[i]-x[0]);
		}
		sort(tan+1,tan+n+1);
		for (i=1;i<=n;i++)
		{
			if (tan[i]!=tan[i+1])
				flag[i] = 1;
			if (flag[i])
				z++;
		}
		printf("%d\n",z);
	}
	return 0;
}