#include<cmath>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
struct emm{
    int l,r;
}a[50007];
bool cmp(emm qaq,emm qwq)
{
    if(qaq.l==qwq.l)return qaq.r<qwq.r;
    return qaq.l<qwq.l;
}
int main()
{
    int n;
    scanf("%d",&n);
   for(int i=1;i<=n;++i)
    scanf("%d%d",&a[i].l,&a[i].r);
    sort(a+1,a+n+1,cmp);
    int l=a[1].l,r=a[1].r;
    for(int i=2;i<=n;++i)
    {
        if(a[i].l<=r)r=max(r,a[i].r);
        else{
            cout<<l<<" "<<r<<endl;
            l=a[i].l,r=a[i].r;
        }
    }
    if(l){cout<<l<<" "<<r<<endl;}
    return 0;
}