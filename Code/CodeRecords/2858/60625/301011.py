#include<stdio.h>
int main()
{
	int a[12][12];
	int i,j,n;
	while(scanf("%d",&n)!=EOF)
	{
			for (i=0,j=0;i<n;i++)
				a[i][j] = 1;
			for (i=0,j=0;j<n;j++)
				a[i][j] = 1;
			int max = 1;
			for (i=1;i<n;i++)
				for (j=1;j<n;j++)
				{
					a[i][j] = a[i-1][j] + a[i][j-1];
					if (max<a[i][j])
						max = a[i][j];
				}
			printf("%d\n",max);
	}
	return 0;
}