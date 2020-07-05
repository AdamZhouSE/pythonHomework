#include<cstdio>
#include<queue>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
using namespace std;
const int M=1e5+9;
int n,m,tot,ans;
int a[M][5],t[M*4],c[10][M*3],f[M][5];
int cnt;
inline void update(int id,int x,int v)
{
    for(;x<=m;x+=x&(-x))
        c[id][x]=max(c[id][x],v);
}
inline int query(int id,int x)
{
    int ans=0;
    for(;x;x-=x&(-x))
        ans=max(ans,c[id][x]);
    return ans;
}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=3;i++)
    for(int j=1;j<=n;j++)
    {
        scanf("%d",&a[j][i]);
        t[++cnt]=a[j][i];
    }
    sort(t+1,t+cnt+1);
    m=unique(t+1,t+cnt+1)-(t+1);
    
    for(int i=1;i<=3;i++)
    for(int j=1;j<=n;j++)
        a[j][i]=lower_bound(t+1,t+m+1,a[j][i])-t;
    for(int i=1;i<=n;i++)
    {
        f[i][1]=max(f[i][1],query(1,a[i][1])+1);
        f[i][1]=max(f[i][1],query(3,a[i][1])+1);
        f[i][1]=max(f[i][1],query(5,a[i][1])+1);
        f[i][1]=max(f[i][1],query(7,a[i][1])+1);
        
        f[i][3]=max(f[i][3],query(1,a[i][3])+1);
        f[i][3]=max(f[i][3],query(3,a[i][3])+1);
        f[i][3]=max(f[i][3],query(5,a[i][3])+1);
        
        f[i][2]=max(f[i][2],query(2,m-a[i][2]+1)+1);
        f[i][2]=max(f[i][2],query(4,m-a[i][2]+1)+1);
        f[i][2]=max(f[i][2],query(6,m-a[i][2]+1)+1);
        f[i][2]=max(f[i][2],query(8,m-a[i][2]+1)+1);
        
        f[i][4]=max(f[i][4],query(2,m-a[i][3]+1)+1);
        f[i][4]=max(f[i][4],query(4,m-a[i][3]+1)+1);
        f[i][4]=max(f[i][4],query(8,m-a[i][3]+1)+1);
        
        update(1,a[i][1],f[i][1]);
        update(2,m-a[i][1]+1,f[i][1]);
        
        update(3,a[i][2],f[i][2]);
        update(4,m-a[i][2]+1,f[i][2]);
        
        update(5,a[i][3],f[i][3]);
        update(6,m-a[i][3]+1,f[i][3]);
    
        update(7,a[i][3],f[i][4]);
        update(8,m-a[i][3]+1,f[i][4]);
        
        for(int j=1;j<=4;j++)
            ans=max(ans,f[i][j]);
    }
    cout<<ans;
    return 0;
}