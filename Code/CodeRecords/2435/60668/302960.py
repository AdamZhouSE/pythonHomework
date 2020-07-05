#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define reg register
#define lson k<<1
#define rson k<<1|1
using namespace std;
const int N=50001,M=300001;
int n,m,i,a,b;
struct tree
{
    int l,r;
    char s[15],ss[15]; //s是转换小写之后的串，ss保存原串 
}t[4*N];  //线段树结构 
inline void read(reg int &x)  //读入优化(虽然并没有什么x用) 
{
    reg int out=0;reg char ch=getchar();
    while (ch<48||ch>57)ch=getchar();
    while (ch>47&&ch<58)
        out=out*10+ch-48,ch=getchar();
    x=out;
}
inline void build(reg int l,reg int r,reg int k)
{
    t[k].l=l;t[k].r=r;
    if (l==r)
    {
        scanf("%s",t[k].s);
        strcpy(t[k].ss,t[k].s);  //把s赋给ss 
        reg int len=strlen(t[k].s);
        for (i=0;i<len;i++)
            t[k].s[i]=tolower(t[k].s[i]);  //转小写比较 
        return;
    }
    reg int mid=(l+r)>>1;
    build(l,mid,lson);
    build(mid+1,r,rson);
    if (strcmp(t[lson].s,t[rson].s)>0) //更新
        strcpy(t[k].s,t[lson].s),strcpy(t[k].ss,t[lson].ss);
    else strcpy(t[k].s,t[rson].s),strcpy(t[k].ss,t[rson].ss);
}
inline int query(reg int l,reg int r,reg int k) //查询 
{
    if (t[k].l>r||t[k].r<l)return 0;
    //如果不属于这个区间就return 0，而t[0].s是"1"，比任何字母的字典序都要小，所以不会取到0 
    if (t[k].l>=l&&t[k].r<=r)return k;
    reg int a=query(l,r,lson),b=query(l,r,rson);
    return strcmp(t[a].s,t[b].s)>0?a:b;
}
int main()
{
    read(n);read(m);
    build(1,n,1);  //建树 
    strcpy(t[0].s,"1");
    for (i=1;i<=m;i++)
        read(a),read(b),printf("%s\n",t[query(a,b,1)].ss);   //记得输出的是原串 
    return 0;
}