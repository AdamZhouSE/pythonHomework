#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;

LL n;
LL dp[105][105] = {0};
LL numlen[105] = {0};
string s;

inline char judge(LL l,LL r,LL L,LL R){ // 判断函数
    register LL len = r - l + 1,k = L - 1;
   // len为折叠部分(i,k)长度 k为目前处理字符位置(判断相等)
    while(1){
        for(register LL i = l;i <= r;i ++){
            k ++;
            if(k > R) return 0;
            if(s[k] != s[i]) return 0;
        // 不断循环(i,k)部分与后面部分匹配,一旦有不同直接return 0
        }
        if(k == R) break; // 只有k==R会返回1,这样如果(i,j)长度不是(i,k)倍数会在上面直接退掉
    }
    return 1;
}

int main(){
    memset(dp,0x3f,sizeof(dp));
    cin >> s;
    n = s.length();
    s = ' ' + s;
    for(register LL i = 1;i <= n;i ++) dp[i][i] = 1; // 预处理dp,(i,i)最短折叠必定为1,其他一开始赋INF
    for(register LL i = 1;i <= n;i ++) numlen[i] = numlen[i / 10] + 1; // 预处理numlen
    for(register LL l = 1;l < n;l ++){ // 从小到大第一维枚举长度
        for(register LL j,i = 1;i < n;i ++){
            j = i + l;
        // i,j 区间左右端点
            if(j > n) break;
            dp[i][j] = l + 1;
            for(register LL k = i;k < j;k ++){
                if(judge(i,k,k + 1,j)) dp[i][j] = min(dp[i][j],dp[i][k] + 2 + numlen[(l + 1) / (k - i + 1)]);
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k + 1][j]); // dp式
            }
        }
    }
    cout << dp[1][n] << endl; // 整个区间最短折叠
    return 0;
}