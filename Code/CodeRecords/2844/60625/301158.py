#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{  int n,m;
   while(~scanf("%d%d",&n,&m)){
         int s[n+1];
         for(int i=1;i<=n;i++) scanf("%d",&s[i]);
         int l=1,r=1;
         int ans=0,temp=0;
         while(r<=n){
              temp+=s[r];
              r++;
              while(temp>m){
                  temp-=s[l];
                  l++;              
              }
              ans=max(ans,r-l);   //更新答案 
         }
         cout<<ans<<endl;
   }
}