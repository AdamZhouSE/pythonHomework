#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<cmath>
#include<bitset>
#define mem(a,b) memset(a,b,sizeof(a))
#define INF 1000000007
#define maxn 100010
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
struct splaytree
{
    int pre[maxn];
    int key[maxn];
    int ch[maxn][2];
    int root,tot;
    splaytree()
    {
        tot=root=0;
        mem(ch,0);
        mem(pre,0);
        mem(key,0);
    }
    void newnode(int &r,int father,int k)
    {
        r=++tot;
        pre[r]=father;
        key[r]=k;
        ch[r][0]=ch[r][1]=0;
    }
    void rotate(int x,int kind)
    {
        int y=pre[x];
        ch[y][!kind]=ch[x][kind];
        pre[ch[x][kind]]=y;
        ch[x][kind]=y;
        if(pre[y]) ch[pre[y]][ch[pre[y]][1]==y]=x;
        pre[x]=pre[y];
        pre[y]=x;
    }
    void splay(int x,int goal) 
    {
        while(pre[x]!=goal)
        {
            if(pre[pre[x]]==goal) rotate(x,ch[pre[x]][0]==x);
            else
            {
                int y=pre[x];
                int kind=ch[pre[y]][0]==y;
                if(ch[y][kind]==x) rotate(x,!kind),rotate(x,kind);
                else rotate(y,kind),rotate(x,kind);
            }
        }
        if(!goal) root=x;
    }
    int insert(int x)
    {
        int r=root;
        while(ch[r][key[r]<x])
        {
            if(key[r]==x) {splay(r,0);return 0;}
            r=ch[r][key[r]<x];
        }
        newnode(ch[r][x>key[r]],r,x);
        splay(ch[r][x>key[r]],0);
        return 1;
    }
    int find(int x)
    {
        int r=root;
        if(!r) return -INF;
        if(key[r]==x) return r;
        while(ch[r][x>key[r]])
        {
            r=ch[r][x>key[r]];
            if(key[r]==x) return r;
        }
        return -INF;
    }
    int get_pre(int x)
    {
        int r=ch[x][0];
        if(!r) return -INF;
        while(ch[r][1]) r=ch[r][1];
        return key[r];
    }
    int get_next(int x)
    {
        int r=ch[x][1];
        if(!r) return INF;
        while(ch[r][0]) r=ch[r][0];
        return key[r];
    }
};
int main()
{
    int sum=0,a,n;
    splaytree tree;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a);
        if(!i)
        {
            sum+=a;
            tree.newnode(tree.root,0,a);
            continue;
        }
        if(!tree.insert(a)) continue;

        int x=tree.get_pre(tree.root);
        int y=tree.get_next(tree.root);
        sum+=min(a-x,y-a);
    }
    cout<<sum;
    return 0;
}