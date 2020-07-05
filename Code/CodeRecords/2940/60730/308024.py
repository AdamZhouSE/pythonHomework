#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#define inf 0x7fffffff
#define ll long long
using namespace std;
inline ll read()
{
    ll x=0,f=1;char ch=getchar();
    while(ch>'9'||ch<'0'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
char s[105];
int f[105][105];
string ans[105][105];
bool mark[105][105];
bool jud(int l,int r,int cl,int cr)
{
     if((r-l+1)%(cr-cl+1)!=0)return 0;
     for(int i=l;i<=r;i++)
        if(s[i]!=s[(i-l)%(cr-cl+1)+cl])return 0;
     return 1;
}
int get(int x)
{int t=0;while(x){x/=10;t++;}return t;}
string getch(int x)
{
	string tmp;
    while(x)
    {
    	tmp=char(x%10+'0')+tmp;
    	x/=10;
    }
    return tmp;
}
int dp(int l,int r)
{
    if(mark[l][r])return f[l][r]; 
    if(l==r){ans[l][r]=s[l];return 1;}
    mark[l][r]=1;
    int t=r-l+1;
    for(int i=l;i<=r;i++)ans[l][r]+=s[i];
    for(int i=l;i<r;i++)
    {
    	int tmp=dp(l,i)+dp(i+1,r);
        if(tmp<t){t=tmp;ans[l][r]=ans[l][i]+ans[i+1][r];}
        if(jud(i+1,r,l,i))
        {
        	int tmp=dp(l,i)+2+get((r-i)/(i-l+1)+1);
            if(tmp<t)
			{
			    t=tmp;
                ans[l][r]=getch((r-i)/(i-l+1)+1)+"("+ans[l][i]+")";
            }
        }
    }
    return f[l][r]=t;
    } 
int main()
{
	//freopen("cipher.in","r",stdin);
	//freopen("cipher.out","w",stdout);
    scanf("%s",s);
    int l=strlen(s);
    dp(0,l-1);
    cout<<ans[0][l-1];
    return 0;
}