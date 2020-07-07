#include<bits/stdc++.h>
using namespace std;
#define N 400001
int lazy[N],s[N];
void add(int k,int l,int r)//添加lazy标记 
{
    if(lazy[k])//如果将要下传的点已经有了标记，就把他去掉然后再修改数据。因为一个点两次修改数据后数值还是和原来的一样。
    {
        lazy[k]=0;
    }else
    lazy[k]=1;
    s[k]=r-l+1-s[k];//剩下的灯光数,修改数据
    return ;
}
void pushdown(int k,int l,int r)//下压1或0
{
    if(lazy[k])
    {
        int mid=(l+r)/2;
        add(k*2,l,mid);
        add(k*2+1,mid+1,r);
        lazy[k]=0;
    }
    return ;
}
void modify(int k,int l,int r,int x,int y)//修改区间灯光数 
{
    if(x>r||y<l)
    return ;
    if(x<=l&&r<=y)
    {
        add(k,l,r);//添加lazy标记 
        return ;
    }
    pushdown(k,l,r);//修改下压 
    int mid=(l+r)/2;
    modify(k*2,l,mid,x,y);
    modify(k*2+1,mid+1,r,x,y);
    s[k]=s[k*2]+s[k*2+1];//修改后维护区间和 
}
int ask(int k,int l,int r,int x,int y)
{
    if(x>r||y<l)//不在修改区间内跳出
    return 0;
    if(x<=l&&r<=y)
    {
        return s[k];
    }
    pushdown(k,l,r);//压
    int mid=(l+r)/2;
    return ask(k*2,l,mid,x,y)+ask(k*2+1,mid+1,r,x,y);//直接求得答案
}
int main()
{
    int n,m,flag;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        scanf("%d",&flag);
        if(flag==1)
        {
            scanf("%d%d",&x,&y);
            printf("%d\n",ask(1,1,n,x,y));
        }
        if(flag==0)
        {
            scanf("%d%d",&x,&y);    
            modify(1,1,n,x,y);
        }   
    }
    return 0;   
}