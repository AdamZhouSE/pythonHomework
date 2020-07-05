
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int a[300010];//点的个数
struct node
{
    int x,y,k,d;//x→y第k小，d：原编号 
} q[51000];//询问 
int ans[51000];//存结果 
int i,j,n,m;
int t[301000];//树状数组 
int h[301000];
bool cmp(node aa,node bb)//关键字1：左端 关键字2：右端 
{
    if (aa.x==bb.x) return aa.y<bb.y;
    return aa.x<bb.x;
} 
void xg(int k,int p)//树状数组之 
{
    while (k<=n)
    {
        t[k]+=p;
        k+= k & -k;
    } 
} 
int qh(int k)
{
    int sum=0;
    while (k>=1)
    {
        sum+=t[k];
        k-= k & -k; 
    } 
    return sum;
}
int main()
{
    scanf("%d%d",&n,&m);
    for (i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
        h[i]=a[i];
    }
    sort(h+1,h+n+1);//h:排好序的数组 
    for (i=1;i<=m;i++)
    {
        scanf("%d%d%d",&q[i].x,&q[i].y,&q[i].k);
        q[i].d=i;
    }
    int he=1;int ta=0;
    sort(q+1,q+m+1,cmp);//排序
    for (i=1;i<=m;i++)
    {
        while (ta<q[i].y)//把之前没有加过的元素加到树状数组中 
        {
            ta++;
            xg(lower_bound(h+1,h+n+1,a[ta])-h,1);//同下 
        }
        while (he<q[i].x)//删去前面加过的元素 
        {
            xg(lower_bound(h+1,h+n+1,a[he])-h,-1);
            he++;
        }
        int l=1;
        int r=n;
        int mid;
        while (l<r)//二分找第k小数 
        { 
            mid=(l+r)>>1;
            if (qh(mid)>=q[i].k) r=mid; else l=mid+1;
        }
        ans[q[i].d]=h[l]; 
    } 
    for (i=1;i<=m;i++) printf("%d\n",ans[i]);
    return 0;
}

