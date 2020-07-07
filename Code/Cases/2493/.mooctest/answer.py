#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
#define maxn 1000119
int num[maxn],tree[maxn],booll[maxn],nnn[maxn],N,ww;;
//num数组保存原数列，tree树状数组，nnn保存结果
struct tt
{
    int l,r;//左右边界
    int pos;//原位置（因为我们要离线排序后处理）
};
tt ask[maxn];
bool cmp(tt x,tt y)
{ 
    return x.r<y.r;
    //快排大法好，没有什么是快排解决不来哦
    //实在不行就加上一个cmp
}
int lowbit(int n) 
{
    return n&(-n);
    //树状数组核心操作×1
}
void add(int n,int now)
{
    while(n<=N)
    {
        tree[n]+=now;
        n+=lowbit(n);
    }
    //树状数组核心操作×2-->更新操作
}
int sum(int n)
{
    int ans=0;
    while(n!=0)
    {
        ans+=tree[n];
        n-=lowbit(n);
    }
    return ans;
    //树状数组核心操作×3———>查询操作
}
int main()
{
        scanf("%d",&N);
        for(int i=1;i<=N;i++)
            scanf("%d",&num[i]);
        scanf("%d",&ww);
        for(int i=1;i<=ww;i++)
        {
            scanf("%d%d",&ask[i].l,&ask[i].r);
            ask[i].pos=i; //存储初始位置
        }
        sort(ask+1,ask+1+ww,cmp);//按r排序
        int next=1;
        for(int i=1;i<=ww;i++)
        {
            for(int j=next;j<=ask[i].r;j++)
            {
                if(booll[num[j]]) 
                    add(booll[num[j]],-1);
                 //之前打过标记，在之前的位置加上-1，保证无重复
                add(j,1);
                booll[num[j]]=j;
            }
            next=ask[i].r+1;
            //更新下一次查询的位置
            nnn[ask[i].pos]=sum(ask[i].r)-sum(ask[i].l-1);
            //按询问编号存储每组询问的结果
        }
    for(int i=1;i<=ww;i++)
      cout<<nnn[i]<<endl;
    return  0;
}