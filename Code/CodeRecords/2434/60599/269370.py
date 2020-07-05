#include<iostream>
#include<cstdio>
#include<cstring>
#define maxN 1000010
#define ls k<<1
#define rs k<<1 | 1
#define mid ((l+r)>>1)
#define node int
#define in(x) x=read()
using namespace std;
inline int read()
{
    int num=0,f=1;
    char ch=getchar();
    while((ch<'0' || ch>'9') && ch!='-') ch=getchar();
    if(ch=='-') {f=-1; ch=getchar();}
    while(ch>='0' && ch<='9')
    {
        num=(num<<3)+(num<<1)+ch-'0';
        ch=getchar();
    }
    return num*f;
}
class segment_tree
{
    public:
        node qmax(int l,int r) {return query(sum1,1,1,1,tot,l,r);}
        node qmin(int l,int r) {return query(sum2,2,1,1,tot,l,r);}
        void build(int k,int l,int r)
        {
            if(l==r) {in(sum1[k]); sum2[k]=sum1[k]; return;}
            build(ls,l,mid); build(rs,mid+1,r);
            sum1[k]=max(sum1[ls],sum1[rs]);
            sum2[k]=min(sum2[ls],sum2[rs]);
        }
        void clear(int n) {memset(sum1,0,sizeof(sum1)); memset(sum2,0x3f,sizeof(sum2)); tot=n;}
    private:
        node sum1[4*maxN+1],sum2[4*maxN+1]; int tot;
        node query(node sum[],int op,int k,int l,int r,int ql,int qr)
        {
            if(ql<=l && r<=qr) return sum[k];
            node maxT=0,minT=0x3f3f3f3f;
            if(ql<=mid) maxT=minT=query(sum,op,ls,l,mid,ql,qr);
            if(op==1 && qr>mid) maxT=max(maxT,query(sum,op,rs,mid+1,r,ql,qr));
            if(op==2 && qr>mid) minT=min(minT,query(sum,op,rs,mid+1,r,ql,qr));
            return (op==1)?maxT:minT;
        }
};
segment_tree tree;
int n,m,c,f=1;
int main()
{
    in(n); in(m); in(c);
    tree.clear(n); tree.build(1,1,n);
    for(int i=1;i<=n-m+1;i++)
        if(tree.qmax(i,i+m-1)-tree.qmin(i,i+m-1)<=c) {printf("%d\n",i); f=0;}
    if(f) printf("NONE");
    return 0;
}