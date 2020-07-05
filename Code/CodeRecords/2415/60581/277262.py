#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int n,a[50],f[50][50],num[50][50],b[50][50][50];
void dfs(int l,int r)
{
    if (f[l][r]!=0) return;
    if (l>r) 
    {
        f[l][r]=1;
        num[l][r]=0;
        return;
    }
    if (l==r) 
    {
        f[l][r]=a[l];
        num[l][r]=1;
        b[l][r][1]=l;
        return;
    }
    for (int i=l;i<=r;i++) 
    {
        dfs(l,i-1);
        dfs(i+1,r);
        if (f[l][i-1]*f[i+1][r]+a[i]>f[l][r]) 
        {
            f[l][r]=f[l][i-1]*f[i+1][r]+a[i];
            num[l][r]=1;
            b[l][r][1]=i;
            for (int j=1;j<=num[l][i-1];j++) b[l][r][++num[l][r]]=b[l][i-1][j];
            for (int j=1;j<=num[i+1][r];j++) b[l][r][++num[l][r]]=b[i+1][r][j];
        }
    }
}
int main()
{
    scanf("%d",&n);
    for (int i=1;i<=n;i++) scanf("%d",&a[i]);
    memset(f,0,sizeof(f));
    dfs(1,n);
    printf("%d\n",f[1][n]);
    for (int i=1;i<=num[1][n]-1;i++) printf("%d ",b[1][n][i]);
    printf("%d ",b[1][n][num[1][n]]); 
    return 0;
}