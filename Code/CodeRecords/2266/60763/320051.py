#include<cstdio>
#include<cctype>
#include<set>
#define RI register int
#define CI const int&
#define Tp template <typename T>
using namespace std;
typedef unsigned long long ull;
const int N=100005; const ull seed=1e9+7;
int n; set <ull> s;
class FileInputOutput
{
    private:
        static const int S=1<<21;
        #define tc() (A==B&&(B=(A=Fin)+fread(Fin,1,S,stdin),A==B)?EOF:*A++)
        char Fin[S],*A,*B;
    public:
        Tp inline void read(T& x)
        {
            x=0; char ch; while (!isdigit(ch=tc()));
            while (x=(x<<3)+(x<<1)+(ch&15),isdigit(ch=tc()));
        }
        #undef tc
}F;
inline ull updata(CI x,CI y)
{
    return x*seed+y;
}
class Tree_Hash_Solver
{
    private:
        struct edge
        {
            int to,nxt;
        }e[N<<1]; int head[N],cnt,deg[N],size[N],g[N],x,y;
    public:
        int n,f[N]; //g only in subtree,f include all tree
        inline void add(CI x,CI y)
        {
            e[++cnt]=(edge){y,head[x]}; head[x]=cnt; ++deg[x];
        }
        inline void init(void)
        {
            for (RI i=1;i<n;++i) F.read(x),F.read(y),add(x,y),add(y,x);
        }
        #define to e[i].to
        inline void DFS1(CI now,CI fa)
        {
            size[now]=g[now]=1; for (RI i=head[now];i;i=e[i].nxt)
            if (to!=fa) DFS1(to,now),size[now]+=size[to],g[now]^=updata(g[to],size[to]);
        }
        inline void DFS2(CI now,CI fa)
        {
            if (!fa) f[now]=g[now]; else f[now]=g[now]^updata(f[fa]^updata(g[now],size[now]),n-size[now]);
            for (RI i=head[now];i;i=e[i].nxt) if (to!=fa) DFS2(to,now);
        }
        #undef to
        inline bool isleaf(CI now)
        {
            return deg[now]==1;
        }
        inline bool check(CI now)
        {
            return s.count(f[e[head[now]].to]^updata(g[now],1));
        }
}A,B;
int main()
{
    //freopen("CODE.in","r",stdin); freopen("CODE.out","w",stdout);
    RI i; for (F.read(n),A.n=n,A.init(),A.DFS1(1,0),A.DFS2(1,0),i=1;i<=n;++i) s.insert(A.f[i]);
    for (B.n=n+1,B.init(),i=1;i<=B.n;++i) if (!B.isleaf(i)) { B.DFS1(i,0); B.DFS2(i,0); break; }
    for (i=1;i<=B.n;++i) if (B.isleaf(i)&&B.check(i)) return printf("%d",i),0; return 0;
}