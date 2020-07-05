#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>

#define L(x) (x<<1)
#define R(x) (x<<1|1)
#define MID(x,y) ((x+y)>>1)

#define bug printf("hihi\n")

#define eps 1e-12

typedef long long ll;

using namespace std;

#define INF 0x3f3f3f3f
#define N 105

string s;
int dp[N][N];
string f[N][N];

int judge(int le,int ri)
{
    int i,j;
    int len=(ri-le+1);
    for(i=1;i<=len/2;i++)
    {
        bool flag=false;
        if(len%i) continue;
        for(j=le;j+i<=ri;j++)
           if(s[j]!=s[j+i]) {flag=true; break;}
        if(!flag) return i;
    }
    return 0;
}

int dfs(int le,int ri)
{
    if(dp[le][ri]!=-1) return dp[le][ri];
    if(le==ri)
    {
        f[le][ri]=s[le];
        dp[le][ri]=1;
        return 1;
    }
    int mid,i;
    dp[le][ri]=ri-le+1+1;

    for(i=le;i<ri;i++)
    {
       int he=dfs(le,i)+dfs(i+1,ri);
       if(he<dp[le][ri])
       {
           dp[le][ri]=he;
           mid=i;
       }
    }
    f[le][ri]=f[le][mid]+f[mid+1][ri];

    int len=judge(le,ri);

    if(len)
    {
        int tt=(ri-le+1)/len;
        char c[100];
        sprintf(c,"%d",tt);
        string temp="";
        temp=c;
        temp=temp+"("+f[le][le+len-1]+")";
        if(temp.length()<dp[le][ri])
        {
            dp[le][ri]=temp.length();
            f[le][ri]=temp;
        }
    }
    return dp[le][ri];
}
int main()
{
    int i,j;
    while(cin>>s)
    {
        int len=s.length();
        memset(dp,-1,sizeof(dp));
        dfs(0,len-1);
        cout<<f[0][len-1]<<endl;
    }
    return 0;
}