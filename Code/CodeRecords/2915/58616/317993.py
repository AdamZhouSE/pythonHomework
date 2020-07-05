#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

int n, a[200000+8], dp[200000+8];

int main()
{
    scanf("%d", &n);
    for(int i = 0; i<n; i++)
        scanf("%d", &a[i]);
    int ans = 1;//寻求最优的结果
    dp[1] = 1;//一开始设最长上升子序列的1
    for(int i = 0; i<n; i++)
        {
            if(a[i-1]<a[i] && 2*a[i-1] >= a[i] && dp[i-1]+1>dp[i])//判断后一个数是不是比前一个数大且小于前一个数的2倍，并且最长上升子序列是否还可以增加
                dp[i] = dp[i-1]+1;
            else dp[i] = 1;
            ans = max(ans, dp[i]);//因为最后一个dp不一定是最长上升子序列，所以要让某个数把最大的结果存起来
        }
    printf("%d\n", ans);
    return 0;
}