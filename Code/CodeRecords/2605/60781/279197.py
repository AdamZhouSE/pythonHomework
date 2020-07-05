#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAX=100005;
int key[MAX],ls[MAX],rs[MAX],fa[MAX],dis[MAX],del[MAX],n,m;
int gi()
{
    int x=0,w=1;char ch=getchar();
    while ((ch<'0'||ch>'9')&&ch!='-') ch=getchar();
    if (ch=='-') w=-1,ch=getchar();
    while (ch>='0'&&ch<='9')
    {
        x=(x<<3)+(x<<1)+ch-'0';
        ch=getchar();
    }
    return x*w;
}

int Merge(int A,int B)
{
    if (!A) return B;
    if (!B) return A;
    if (key[A]>key[B]||(key[A]==key[B]&&A>B)) swap(A,B);
    rs[A]=Merge(rs[A],B);
    fa[rs[A]]=A;
    if (dis[ls[A]]<dis[rs[A]]) swap(ls[A],rs[A]);
    dis[A]=dis[rs[A]]+1;
    return A;
}
void Delete(int A)
{
    del[A]=1;
    fa[ls[A]]=fa[rs[A]]=0;
    Merge(ls[A],rs[A]);
}
int find(int x)
{
    while (fa[x]) x=fa[x];
    return x;
}
int main()
{
    n=gi();m=gi();
    for (int i=1;i<=n;i++) key[i]=gi();
    while (m--)
    {
        int opt=gi();
        if (opt==1)
        {
            int x=gi(),y=gi();
            int fx=find(x),fy=find(y);
            if (del[x]||del[y]||fx==fy) continue;
            Merge(fx,fy);
        }
        else
        {
            int x=gi();
            if (del[x]) printf("-1\n");
            else
            {
                int fx=find(x);
                printf("%d\n",key[fx]);
                Delete(fx);
            }
        }
    }
    return 0;
}