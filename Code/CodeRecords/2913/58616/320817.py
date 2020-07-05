#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
int main()
{
	int n;
	scanf("%d",&n);
	long long a[n];
	long long  maxx=0;
	long long sum=0;
	int flag=0;//表示是否成功 
	for(int i=0;i<n;i++)
	{
		scanf("%lld",&a[i]);
	    maxx=max(maxx,a[i]);
	    sum+=a[i];
	}
	long long mid=sum/2;
	if(sum%2!=0)
	flag=1;		
	if(maxx>mid)
	flag=1;
    
    if(flag==1)
    printf("NO\n");
    else 
    printf("YES\n");
}