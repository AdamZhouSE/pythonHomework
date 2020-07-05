#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

const int maxn=100+10;
const int INF=1000000;
int dp[maxn][maxn];
string flod[maxn][maxn];
string str;
int judge(int L,int R)
{
    for(int i=1;i<=(R-L+1)/2;i++){
        if((R-L+2)%i)continue;//不能分为整数段
        bool flag=true;
        for(int j=L;j+i<=R;j++){
            if(str[j]!=str[j+i]){
                flag=false;
                break;
            }
        }
        if(flag)return i;
    }
    return 0;
}
int solve(int L,int R)
{
    int& ans=dp[L][R];
    if(ans!=-1)return ans;
    if(L==R){
        flod[L][R]=str[L];
        return ans=1;
    }
    ans=INF;
    int k,t;
    for(int i=L;i<=R;i++){
        t=solve(L,i)+(i+1,R);
        if(t<ans){
            ans=t;
            k=i;
        }
    }
    flod[L][R]=flod[L][k]+flod[k+1][R];
    int len=judge(L,R);
    if(len){
        bool test=true;
        for(int i=L;i<=R;i++){
            if(str[i]=='('||str[i]==')')test=false;//不能把括号作为压缩对象
        }
        char t[10];
        sprintf(t,"%d",(R-L+1)/len);
        string newstr=t+string("(")+flod[L][L+len-1]+string(")");
        if(test&&newstr.size()<ans){
            ans=newstr.size();
            flod[L][R]=newstr;
        }
    }
    return ans;
}
int main()
{
    while(cin>>str){
        memset(dp,-1,sizeof(dp));
        int len=str.size()-1;
        solve(0,len);
        cout<<flod[0][len]<<endl;
    }
    return 0;
}