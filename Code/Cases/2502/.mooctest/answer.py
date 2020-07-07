#include<iostream>
using namespace std;
long long a[1000005];//每个数的值
int main(void)
{
    long long n,ans=0;//n表示数的数量，ans是代价
    cin>>n;//输入数的个数
    for(int i=1;i<=n;i++)
    {
        cin>>a[i];//整个程序大部分时间都花在这步上了qwq
    }
    for(int i=1;i<=n;i++)//枚举每个数
    {
        if(i>1&&a[i-1]<a[i])//如果左边小于它
        {
            ans+=a[i];
        }
        if(i<n&&a[i+1]<=a[i])//如果右边小于等于它
        {
            ans+=a[i];
        }
    }
    cout<<ans<<endl;//输出
    return 0;
}