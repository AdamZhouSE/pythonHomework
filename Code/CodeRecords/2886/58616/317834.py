#include <iostream>  
#include <cstdio>  
#include <string>  
#include <cstring>  
#include <algorithm>  
#include <cmath>  
#include <queue>  
#include <vector>  
#include <set>  
#include <stack>  
#include <map>  
#include <climits>  
  
using namespace std;  
  
#define LL long long  
const int INF=0x3f3f3f3f;  
  
int a[100090],n;  
  
int main()  
{  
while(~scanf("%d",&n))  
{  
int k,sum=0,ma=0;  
memset(a,0,sizeof a);  
for(int i=1;i<=2*n;i++)  
{  
scanf("%d",&k);  
if(a[k]) a[k]--,sum--;  
else sum++,ma=max(sum,ma),a[k]++;  
}  
printf("%d\n",ma);  
}  
return 0;  
}  