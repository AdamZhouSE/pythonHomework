#include<cstdio>
#include<algorithm>
#include<cmath>
#define N 100050
using namespace std;
int n,m;
int l,r;
int a[N];
int f[N][30];
int main()
 {
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);

    for(int i=1;i<=n;i++)
     f[i][0]=a[i];
    for(int j=1;(1<<j)<=n;j++)
     for(int i=1;i+(1<<(j-1))-1<=n;i++)
      f[i][j]=min(f[i][j-1],f[i+(1<<(j-1))][j-1]); 

     for(int i=1;i<=m;i++)
      { 
       scanf("%d%d",&l,&r);
      // while ((1 << (k + 1)) <= r - l + 1) k++;
      int k=int(log2(r-l+1));
       printf("%d ",min(f[l][k],f[r-(1<<k)+1][k]));
      }

 }