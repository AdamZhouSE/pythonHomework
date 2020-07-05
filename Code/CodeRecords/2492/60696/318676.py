#include <algorithm>
#include <cstdio>

inline void read(int &x)
{
    x=0; register char ch=getchar();
    for(; ch>'9'||ch<'0'; ) ch=getchar();
    for(; ch>='0'&&ch<='9'; ch=getchar()) x=x*10+ch-'0';
}
const int N(523);
int c,n;
struct Node {
    int x,y;
    bool operator < (const Node&a)const
    {
        return x<a.x;
    }
}pos[N];

int L,R,Mid,ans,cnt,tmp[N];
inline bool judge(int l,int r)
{
    if(r-l+1<c) return 0; cnt=0;
    for(int i=l; i<=r; ++i) tmp[++cnt]=pos[i].y;
    std::sort(tmp+1,tmp+cnt+1);
    for(int i=c; i<=cnt; ++i)
        if(tmp[i]-tmp[i-c+1]<=Mid) return 1;
    return 0;
}
inline bool check(int x)
{
    int l=1,r=1;
    for(; r<=n; ++r)
    {
        if(pos[r].x-pos[l].x>x)
            if(judge(l,r-1)) return 1;
        for(; pos[r].x-pos[l].x>x; ) l++;
    }
    return judge(l,n);
}

int Presist()
{
    read(c),read(n);
    for(int i=1; i<=n; ++i)
        read(pos[i].x),read(pos[i].y);
    std::sort(pos+1,pos+1+n);
    for(R=1e4; L<=R; )
    {
        Mid=L+R>>1;
        if(check(Mid))
        {
            R=Mid-1;
            ans=Mid+1;
        }
        else L=Mid+1;
    }
    printf("%d\n",ans);
    return 0;
}

int Aptal=Presist();
int main(int argc,char**argv){;}