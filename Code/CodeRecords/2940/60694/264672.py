// https://blog.csdn.net/HownoneHe/article/details/52186657?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
// 区间dp， 看不懂

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#define fo(i,a,b) for (int i=a;i<=b;i++)
#define fd(i,a,b) for (int i=a;i>=b;i--)
#define INF 2147483647
#define N 105
using namespace std;
char s[N];
int F[N][N];
string ans[N][N];
bool bz[N][N];
inline int read()
{
    int x=0,w=1;
    char ch=getchar();
    while(ch>'9'||ch<'0'){if(ch=='-')w=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*w;
}
bool Check(int l,int r,int ll,int rr)
{
    if ((r-l+1)%(rr-ll+1)!=0) return false;
    fo(i,l,r)
        if (s[i]!=s[(i-l)%(rr-ll+1)+ll]) return false;
    return true;
}

int Ask(int x){int y=0;for (;x;x/=10) y++;return y;}
string Get(int x){string t;for (;x;x/=10) t=char(x%10+'0')+t;return t;}
int Dp(int l,int r)
{
    if (bz[l][r]) return F[l][r];
    if (l==r) 
    {
        ans[l][r]=s[l];
        return 1;
    }
    bz[l][r]=true;
    int mn=r-l+1;
    fo(i,l,r) ans[l][r]+=s[i];
    fo(i,l,r-1)
    {
        int temp=Dp(l,i)+Dp(i+1,r);
        if (temp<mn)
        {
            mn=temp;
            ans[l][r]=ans[l][i]+ans[i+1][r];
        }
        if (Check(i+1,r,l,i))
        {
            int temp=Dp(l,i)+Ask((r-i)/(i-l+1)+1)+2;
            if (temp<mn)
            {
                mn=temp;
                ans[l][r]=Get((r-i)/(i-l+1)+1)+"("+ans[l][i]+")";
            }
        }
    }
    return F[l][r]=mn;
}

int main()
{
    scanf("%s",s+1);
    int l=strlen(s+1);
    Dp(1,l);
    cout<<ans[1][l]<<endl;
    return 0;
}