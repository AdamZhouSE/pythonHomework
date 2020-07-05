#include<iostream>
 #include<algorithm>
 #include<cstring>
 using namespace std;
 bool cmpchar(char ta,char tb){
     return ta<tb;
  }
  bool cmpstr(string ta,string tb){
      return ta<tb;
 }
 string word[10001];
 int n;
 int main()
 {
     cin>>n;
     int ans=1;
     for(int i=0;i<n;i++){
         cin>>word[i];
         sort(&word[i][0],&word[i][word[i].size()],cmpchar);
     }
     sort(&word[0],&word[n],cmpstr);
     for(int i=0;i<n-1;i++) 
         if(word[i]!=word[i+1])
         ans++;
     cout<<ans;
     return 0;
 }