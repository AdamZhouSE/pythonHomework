#include<cstdio>
#include<algorithm>
using namespace std; 
int n,ans=1e9; 
int gcd(int a,int b)
{
    if (b==1) return a-1; //因为b不能等于0，所以这里a要减1
    else if (!b) return 1e9; //当b=0时，返回一个较大的值
    else return a/b+gcd(b,a%b); //a/b是为了加快更相减损法（常用于高精度，因为高精度里很难像欧几里得算法一样取模）里的减法（or 加法）
}
int main()
{
    scanf("%d",&n); 
    for (int i=1;i<(n+1);i++)  ans=min(ans,gcd(n,i)); 
    printf("%d",ans); 
}