#include<bits/stdc++.h>
 using namespace std;
 int n,i,j,k,l,r,ans;
 int ne[1300][3],cnt[1300],f[1300][3][1300],s[5][20][50];
 int read()
{
    int x=0,w=0;char ch=0;
    while (!isdigit(ch)) w|=ch=='-',ch=getchar();
    while (isdigit(ch)) x=(x<<1)+(x<<3)+(ch^48),ch=getchar();
    return w?-x:x;
}
 void build(int a,int b){ne[a][cnt[a]++]=b; ne[b][cnt[b]++]=a;}
 int dp(int now,int a,int b)//now为当前节点的值，b为父亲的值，a为另一边界
{
    int fa=0; while(ne[now][fa]!=b)fa++;//寻找父亲是相邻的第几个点
    if(f[now][fa][a])return f[now][fa][a];
    int x,y,l=0,r=0;
    if(a>b)x=b+1,y=a; else x=a,y=b-1;
    for(int i=0;i<3;i++) if(i!=fa&&x<=ne[now][i]&&ne[now][i]<=y)
    {
        if (ne[now][i]<now)l=max(l,dp(ne[now][i],x,now));
        else r=max(r,dp(ne[now][i],y,now));
    }
    f[now][fa][a]=l+r+1;
    return f[now][fa][a];
}//记忆话搜索
 int main()
{
    n=read();
    for(i=1;i<=4;i++)
     for(j=1;j<=n;j++)
      for(k=1;k<j+j;k++) s[i][j][k]=read();
    for(i=1;i<=4;i++)
        for(j=2;j<=n;j++)
        {
            for(k=2;k<j<<1;k+=2)
            {
                build(s[i][j][k],s[i][j-1][k-1]); build(s[i][j][k],s[i][j][k-1]);
                build(s[i][j][k],s[i][j][k+1]);
            }
        }
    for(i=1;i<=n;i++)
    {
        build(s[1][i][1],s[3][i][(i<<1)-1]); 
        build(s[2][i][1],s[1][i][(i<<1)-1]);
        build(s[3][i][1],s[2][i][(i<<1)-1]); 
        build(s[4][i][1],s[1][n][2*n-(i<<1)+1]);
        build(s[4][i][(i<<1)-1],s[2][n][(i<<1)-1]); 
        build(s[4][n][(i<<1)-1],s[3][n][2*n-(i<<1)+1]);
    }//建边
    for(i=1;i<=4*n*n;i++)//枚举根
    {
        l=0; r=0;//记录最大左右子树
        for(j=0;j<3;j++)
         if(ne[i][j]<i)l=max(l,dp(ne[i][j],1,i));
         else r=max(r,dp(ne[i][j],4*n*n,i));
        ans=max(ans,l+r+1);
    }
    cout<<ans<<endl;
    return 0;}