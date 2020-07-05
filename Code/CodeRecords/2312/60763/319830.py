#include<bits/stdc++.h>
using namespace std;
int main(){
    //当节点个数n确定时 能组成的二叉树结构个数也是确定的
    // n个节点中1，2，...n均可做根节点
    // ans = f(1) + f(2) + ... + f(n)  f(i)表示当i做根节点时有几种结构
    // i为根，则说明左子树有i-1个节点，右子树有n-i个节点 f(i) = f(i-1) * f(n-i)
    // 存在重叠子问题，可dp解决
    int n;
    cin>>n;
    int mod = 1e9 + 7;
    vector<long>dp(n+1,0);
    dp[0] = 1;
    dp[1] = 1;
    for(int i=2;i<=n;++i){
        for(int j=0;j<i;++j)
        {
            dp[i] += ((dp[j]%mod) * (dp[i-j-1]%mod));
            dp[i]%=mod;
        }
    }
    cout<<dp[n]<<endl;
    return 0;
}