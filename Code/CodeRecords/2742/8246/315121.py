#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<bits/stdc++.h>
#include<cstring>
using namespace std;
int size[500001],son[500001][2],rd[500001],val[500001];
int T,tot,n,m,x,y,z,opt,a,root,com;
inline void update(int x)
{
    size[x]=1+size[son[x][0]]+size[son[x][1]];
}
inline int new_node(int x)
{
    size[++tot]=1;
    val[tot]=x;
    rd[tot]=rand();
    return tot;
}
int merge(int A,int B)
{
    if (!A||!B) 
        return  A+B;
    if (rd[A]<rd[B])
    {
        son[A][1]=merge(son[A][1],B); 
        update(A); 
        return A;
    }
    else 
    {
        son[B][0]=merge(A,son[B][0]); 
        update(B); 
        return B;
    } 
}
void split(int now,int k,int &x,int &y)
{
    if(!now) 
        x=y=0;
    else 
    {
        if (val[now]<=k) 
            x=now,split(son[now][1],k,son[now][1],y);
        else 
            y=now,split(son[now][0],k,x,son[now][0]);
        update(now);
    }
}
int kth(int now,int k)
{
    while(1)
    {
        if (k<=size[son[now][0]]) 
            now=son[now][0];
        else 
            if (k==size[son[now][0]]+1) 
                return now;
            else 
                k-=size[son[now][0]]+1,now=son[now][1];
    }
}

int main()
{
    srand((unsigned)time(NULL));
    cin>>T;
    while (T--)
    {
        scanf("%d%d",&opt,&a);
        if (opt==1)
        {
            split(root,a,x,y);
            root=merge(merge(x,new_node(a)),y);
        }
        if (opt==2)
        {
            split(root,a,x,z);
            split(x,a-1,x,y);
            y=merge(son[y][0],son[y][1]);
            root=merge(merge(x,y),z);
        }
        if (opt==3)
        {
            split(root,a-1,x,y);
            printf("%d\n",size[x]+1);
            root=merge(x,y);
        }
        if (opt==4) 
            printf("%d\n",val[kth(root,a)]);
        if (opt==5)
        {
            split(root,a-1,x,y);
            printf("%d\n",val[kth(x,size[x])]);
            root=merge(x,y);
        }
        if (opt==6)
        {
            split(root,a,x,y);
            printf("%d\n",val[kth(y,1)]);
            root=merge(x,y);
        }
    }
}