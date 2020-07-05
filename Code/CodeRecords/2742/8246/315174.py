#include <stdio.h>
#include <iostream>
using namespace std;
const int maxt=6e5*32;
const int maxn=6e5;
int ch[maxt][2]={0},size[maxt]={0};
int mem=0,root[maxn];
void insert(int& x,int y,int v)
{
    x=++mem;
    v+=1e9;
    size[x]=size[y]+1;
    int p=x,q=y;
    for(int i=31;i>=0;i--)
    {
        if(v&(1<<i))
        {
            ch[p][1]=++mem;
            ch[p][0]=ch[q][0];

            p=ch[p][1];
            q=ch[q][1];
        }
        else
        {
            ch[p][0]=++mem;
            ch[p][1]=ch[q][1];

            p=ch[p][0];
            q=ch[q][0];
        }
        size[p]=size[q]+1;
    }
}
void erase(int& x,int y,int v)
{
    int q=y;
    v+=1e9;

    for(int i=31;i>=0;i--)
    {
        if(v&(1<<i))
            q=ch[q][1];
        else
            q=ch[q][0];
        if(!q||!size[q])
        {
            x=y;
            return;
        }
    }
    x=++mem;
    size[x]=size[y]-1;
    int p=x;
    q=y;
    for(int i=31;i>=0;i--)
    {
        if(v&(1<<i))
        {
            ch[p][1]=++mem;
            ch[p][0]=ch[q][0];

            p=ch[p][1];
            q=ch[q][1];
        }
        else
        {
            ch[p][0]=++mem;
            ch[p][1]=ch[q][1];

            p=ch[p][0];
            q=ch[q][0];
        }
        size[p]=size[q]-1;
    }
}
int getsmaller(int x,int v)
{
    v+=1e9;
    int p=x;
    int ret=0;
    for(int i=31;i>=0;i--)
    {
        if(v&(1<<i))
        {
            ret+=size[ch[p][0]];
            p=ch[p][1];
        }
        else
            p=ch[p][0];
        if(!p||!size[p])
            return ret;
    }
    return ret;
}
int getbigger(int x,int v)
{
    v+=1e9;
    int p=x;
    int ret=0;
    for(int i=31;i>=0;i--)
    {
        if(v&(1<<i))
            p=ch[p][1];
        else
        {
            ret+=size[ch[p][1]];
            p=ch[p][0];
        }
        if(!p||!size[p])
            return ret;
    }
    return ret;
}
int getvalue(int x,int rank)
{
    int p=x;
    int ret=-1e9;
    for(int i=31;i>=0;i--)
    {
        if(rank>size[ch[p][0]])
        {
            rank-=size[ch[p][0]];
            p=ch[p][1];
            ret+=(1<<i);
        }
        else
            p=ch[p][0];
    }
    return ret;
}
int n,his=0;
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        int v,opt,x;
        scanf("%d%d%d",&v,&opt,&x);
        if(opt==1)
            insert(root[i],root[v],x);
        else if(opt==2)
            erase(root[i],root[v],x);
        else if(opt==3)
        {
            root[i]=root[v];
            cout<<getsmaller(root[v],x)+1<<endl;
        }
        else if(opt==4)
        {
            root[i]=root[v];
            cout<<getvalue(root[v],x)<<endl;
        }
        else if(opt==5)
        {
            root[i]=root[v];
            int sm=getsmaller(root[v],x);
            if(!sm)
                cout<<-2147483647<<endl;
            else
                cout<<getvalue(root[v],sm)<<endl;
        }
        else
        {
            root[i]=root[v];
            int gm=getbigger(root[v],x);
            if(!gm)
                cout<<2147483647<<endl;
            else
                cout<<getvalue(root[v],size[root[v]]-gm+1)<<endl;
        }
    }
    return 0;
}