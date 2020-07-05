#define ui unsigned int
#include<bits/stdc++.h>
#define ll long long

#define db double

#define ld long double

#define ull unsigned long long

const int MAXN=200000+10;

int n,s,k,e,a[MAXN],b[MAXN],beg[MAXN],nex[MAXN],to[MAXN],val[MAXN],ext[MAXN],vis[MAXN],use[MAXN],cnt;

std::vector<int> V,ans[MAXN];

std::map<int,int> M;

template<typename T> inline void read(T &x)

{

    T data=0,w=1;

    char ch=0;

    while(ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();

    if(ch=='-')w=-1,ch=getchar();

    while(ch>='0'&&ch<='9')data=((T)data<<3)+((T)data<<1)+(ch^'0'),ch=getchar();

    x=data*w;

}

template<typename T> inline void write(T x,char ch='\0')

{

    if(x<0)putchar('-'),x=-x;

    if(x>9)write(x/10);

    putchar(x%10+'0');

    if(ch!='\0')putchar(ch);

}

template<typename T> inline void chkmin(T &x,T y){x=(y<x?y:x);}

template<typename T> inline void chkmax(T &x,T y){x=(y>x?y:x);}

template<typename T> inline T min(T x,T y){return x<y?x:y;}

template<typename T> inline T max(T x,T y){return x>y?x:y;}

inline void discretization()

{

    for(register int i=1;i<=n;++i)V.push_back(a[i]);

    std::sort(V.begin(),V.end());

    V.erase(std::unique(V.begin(),V.end()),V.end());

    for(register int i=0,lt=V.size();i<lt;++i)M[V[i]]=i+1;

}

inline void insert(int x,int y,int z)

{

    to[++e]=y;

    nex[e]=beg[x];

    beg[x]=e;

    val[e]=z;

}

inline void dfs(int x)

{

    vis[x]=cnt;

    for(register int &i=beg[x];i;i=nex[i])

        if(!use[i])

        {

            int tmp=i;

            use[i]=1;

            dfs(to[i]);

            ans[cnt].push_back(val[tmp]);

        }

}

int main()

{

    read(n);read(s);

    for(register int i=1;i<=n;++i)read(a[i]);

    discretization();

    for(register int i=1;i<=n;++i)a[i]=b[i]=M[a[i]];

    std::sort(b+1,b+n+1);

    for(register int i=1;i<=n;++i)

        if(a[i]!=b[i])++k,insert(a[i],b[i],i);

    if(k>s)

    {

        puts("-1");

        return 0;

    }

    for(register int i=1;i<=n;++i)

        if(!vis[i]&&beg[i])++cnt,dfs(i);

    if(cnt<=1||s-k<=1)

    {

        printf("%d\n",cnt);

        for(register int i=1;i<=cnt;++i)

        {

            printf("%d\n",ans[i].size());

            for(register int j=0,lt=ans[i].size();j<lt;++j)printf("%d ",ans[i][j]);

            puts("");

        }

        return 0;

    }

    printf("%d\n",cnt-min(s-k,cnt)+2);

    for(register int i=s-k+1;i<=cnt;++i)

    {

        printf("%d\n",ans[i].size());

        for(register int j=0,lt=ans[i].size();j<lt;++j)printf("%d ",ans[i][j]);

        puts("");

    }

    if(s-k)

    {

        int p1=0,p2=0;

        for(register int i=min(s-k,cnt);i>=1;--i)p1+=ans[i].size(),ext[++p2]=ans[i][0];

        printf("%d\n",p1);

        for(register int i=1;i<=min(s-k,cnt);++i)

            for(register int j=0,lt=ans[i].size();j<lt;++j)printf("%d ",ans[i][j]);

        puts("");

        printf("%d\n",p2);

        for(register int i=1;i<=p2;++i)printf("%d ",ext[i]);

    }

    return 0;

}