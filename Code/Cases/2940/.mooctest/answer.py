#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define N 105
string s,ss[N][N];
int n,f[N][N];
inline int jud(int l,int r)
{
    int i,j,bo;
    for(i=1;i<=(r-l+1)/2;i++)
    {
        if(((r-l+1)%i)==0)
        {
            bo=0;for(j=l;j+i<=r;j++)if(s[j]!=s[j+i]){bo=1;break;}if(!bo)return i;
        }
    }return -1;
}
inline int dfs(int l,int r)
{
    if(f[l][r]!=-1)return f[l][r]; if(l==r){f[l][r]=1;ss[l][r]=s[l];return 1;}
    int re=1e5,po,i,tmp;
    for(i=l;i<r;i++)
    {
        tmp=dfs(l,i)+dfs(i+1,r); if(re>tmp){re=tmp;po=i;}
    }ss[l][r]=ss[l][po]+ss[po+1][r]; int le=jud(l,r);
    if(le!=-1)
    {
        string t,nes;char ch; tmp=(r-l+1)/le;
        while(tmp){ch=tmp%10+'0';t.push_back(ch);tmp/=10;} reverse(t.begin(),t.end());
        nes=t+(string)("(")+ss[l][l+le-1]+(string)(")");
        if(nes.size()<re){re=nes.size();ss[l][r]=nes;}
    }return f[l][r]=re;
}
int main()
{
    int i; memset(f,-1,sizeof f); cin>>s; n=s.size(); dfs(0,n-1); cout<<ss[0][n-1]<<endl;
}