#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#define fo(i,a,b) for (int i=a;i<=b;i++)
#define N 1000005

using namespace std;

typedef long long ll;

int n,tot = 0,v = 0;
char Stack[N * 2];
int Root[N],Len[N]; 

struct node
{
    int l,r;
}a[N * 2];

inline int read()
{
    int x=0,w=1;
    char ch=getchar();
    while(ch>'9'||ch<'0'){if(ch=='-')w=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*w;
}

void Update(int &y,int x,int l,int r,int pos,char c)
{
    y = ++ tot;
    if (l == r) Stack[y] = c;
    else
    {
        int mid = (l + r) >> 1;
        a[y].l = a[x].l, a[y].r = a[x].r;
        if (pos <= mid) Update(a[y].l,a[x].l,l,mid,pos,c);
        else Update(a[y].r,a[x].r,mid + 1,r,pos,c);
    }
}

void Query(int y,int l,int r,int pos)
{
    if (l == r) printf("%c\n",Stack[y]);
    else
    {
        int mid = (l + r) >> 1;
        if (pos <= mid ) Query(a[y].l,l,mid,pos);
        else Query(a[y].r,mid + 1,r,pos);
    }
}

int main()
{
    n = read();
    while (n --)
    {
        char cmd[2],s[2];
        scanf("%s",cmd);
        if (cmd[0] == 'T')
        {
            scanf("%s",s);
            Len[++ v] = Len[v - 1] + 1;
            Update(Root[v],Root[v - 1],1,N,Len[v],s[0]);
        }
        else 
        if (cmd[0] == 'U')
        {
            int x = read();
            Root[++ v] = Root[v - x -1];
            Len[v] = Len[v - x - 1];
        }
        else Query(Root[v],1,N,read());
    }
}
