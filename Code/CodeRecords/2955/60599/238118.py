#include<bits/stdc++.h>
#include<vector>
using namespace std;
string a,b;
int k;
int dp[10001][10001];
int main(){
   cin>>a>>b>>k;
   int lena=a.size();
   int lenb=b.size();
   for(int j=1;j<=lena;j++){
      dp[j][0]=j*k;               //
   }
   for(int j=1;j<=lenb;j++){
      dp[0][j]=j*k;    
   }                              // 预处理 当他们所有的碰见的都是空格的时候
   for(int j=1;j<=lena;j++){
      for(int i=1;i<=lenb;i++){
         int t=abs(a[j-1]-b[i-1]); //ASCII 差值
         dp[j][i]=min(min(dp[j-1][i],dp[j][i-1])+k,dp[j-1][i-1]+t);   //第第一个取j个单词  到第 二 个取  i 个单词的最优解 
      }
   }
   cout<<dp[lena][lenb];
 
   return 0;
}
