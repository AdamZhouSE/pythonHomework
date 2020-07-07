#include<cstdio>
#include<algorithm>
struct P{int x,y;int operator<(const P&t)const{return x<t.x;}}e[200010];
int l,n,m,i,w,ans;char c;
inline void R(int &x){c=getchar();for(;c<48||c>57;c=getchar());for(x=0;c>47&&c<58;c=getchar())x=(x<<1)+(x<<3)+c-48;}
main()
{
    R(n);R(m);
    for(i=0;i<n;++i)
    {
        R(l);e[i<<1].x=w;
        if(getchar()=='L')
        {
            e[i<<1].y=-1;
            e[i<<1|1]=(P){w-=l,+1};
        }else
        {
            e[i<<1].y=+1;
            e[i<<1|1]=(P){w+=l,-1};
        }
    }std::sort(e,e+(n<<1));
    w=e[0].y;
    for(i=0;i+1<n<<1;w+=e[++i].y)
        if(w>=m)ans+=e[i+1].x-e[i].x;
    printf("%d",ans);
}