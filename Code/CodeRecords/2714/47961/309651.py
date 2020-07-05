//#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<time.h>
#include<stdio.h>
#include<string.h>
#define srd srand(time(0))
#define ll long long
#define con continue
#define gtc getchar()
#define ptc putchar
#define dou double
#define eps 0.00000000001
#define opr operator
#define cl(x,a) memset(x,a,sizeof(x))
#define fo0(i,k) for(i=fr[k];i;i=nx[i])
#define fo1(i,l,r) for(i=l;i<=r;i++)
#define fo2(i,l,r) for(i=l;i>=r;i--)
#define fo(i,n) for(i=1;i<=n;i++)
#define ret return
#define x first
#define cint const int
#define y second
#define opi(x) freopen(x,"r",stdin)
#define opo(x) freopen(x,"w",stdout)
#define tpl template<class T>
#define priq priority_queue
#define mp make_pair
#define use using namespace
#define WT while(T--)
use std;
typedef pair<int,int> pii;typedef pair<int,ll> pil;typedef pair<ll,int> pli;typedef pair<ll,ll> pll;
namespace io
{
    void _(int &k){char c;int e=1;k=0;while((c=gtc)>'9'||c<'0')if(c=='-')e=-1;k=c-'0';while((c=gtc)<='9'&&c>='0'){k*=10;k+=c-'0';}k*=e;}
    void _(ll &k){char c;int e=1;k=0;while((c=gtc)>'9'||c<'0')if(c=='-')e=-1;k=c-'0';while((c=gtc)<='9'&&c>='0'){k*=10;k+=c-'0';}k*=e;}
    void _(char &c){while((c=gtc)==' '||c=='\n');}void _(dou &c){scanf("%lf",&c);}template<class t1,class t2>void _(t1 &a,t2 &b){_(a);_(b);}
    template<class t1,class t2,class t3>void _(t1 &a,t2 &b,t3 &c){_(a);_(b);_(c);}
    template<class t1,class t2,class t3,class t4>void _(t1 &a,t2 &b,t3 &c,t4 &d){_(a);_(b);_(c);_(d);}
    template<class t1,class t2,class t3,class t4,class t5>void _(t1 &a,t2 &b,t3 &c,t4 &d,t5 &e){_(a);_(b);_(c);_(d);_(e);}
    void _p(dou k){printf("%.6lf",k);}
    tpl void _p0(T k){if(k>=10)_p0(k/10);ptc(k%10+'0');}tpl void _p(T k){if(k<0){ptc('-');_p0(-k);}else _p0(k);}tpl void __p(T k){_p(k);ptc(' ');}
    tpl void _pn(T k){_p(k);ptc('\n');}template<class t1,class t2>void _p(t1 a,t2 b){__p(a);_pn(b);}
    template<class t1,class t2,class t3>void _p(t1 a,t2 b,t3 c){__p(a);__p(b);_pn(c);}
    template<class t1,class t2,class t3,class t4>void _p(t1 a,t2 b,t3 c,t4 d){__p(a);__p(b);__p(c);_pn(d);}
    tpl void op(T *a,int n){int i;n--;fo(i,n)__p(a[i]);_pn(a[n+1]);}int gi(){int x;_(x);ret x;}ll gll(){ll x;_(x);ret x;}
}
int gcd(int a,int b){ret b?gcd(b,a%b):a;}void fop(const char *s){char c[256],d[256];cl(c,0);cl(d,0);strcpy(c,s);strcpy(d,s);opi(strcat(c,".in"));opo(strcat(d,".out"));}void fcl(){fclose(stdin);fclose(stdout);}
int eq(dou a,dou b){return a+eps>=b&&b+eps>=a;}tpl void _ma(T &a,T b){if(a<b)a=b;}tpl void _mi(T &a,T b){if(a>b)a=b;}
cint N=1234567,EE=100000000,GG=1000000000,ima=2147483647;
use io;
int n,m,so[266666][101],v[266666],a[11111][33],f[N],p[N],an,T,z=1;
char s[11111][111],s1[11111][111];
pii c[11111];//pair<int,int> 
void ins(int *a,int b)//插入trie树，注意这个trie的字符集是100，字符串长度是26 
{
    int i,k=1;
    fo1(i,0,25)//i从1到25循环，下同 
    {
        int &t=so[k][a[i]];//t就是要找的下一个节点 
        k=t=t?t:++z;//存在就转移过去，不存在就新建再转移过去 
    }
    v[k]=b;
}
int fi(int *a)//查找和插入非常相似 
{
    int i,k=1;
    fo1(i,0,25)
    {
        int &t=so[k][a[i]];
        if(!(k=t=t?t:0))
            ret 0;
    }
    ret v[k];
}
void op(int k)//这个是为了dp方案的输出，由于记得是pre，所以为了实现正序输出就利用了栈的性质 
{
    if(!k)
        ret;
    op(p[k]);
    puts(s[k]);
}
int main()
{
    int i,j,a1,a2,t,ma,mx=0;
    for(n=1;scanf("%s",s1[n])+1;n++);n--;
    fo(i,n)//这个就是i从1循环到n，下同 
    {
        c[i].y=i;//字符串按长度排序 
        c[i].x=strlen(s1[i]);//x是first,y是second 
    }
    sort(c+1,c+n+1);
    fo(i,n)
    {
        strcpy(s[i],s1[c[i].y]);//这样s就是排序好的字符串数组 
        for(j=0;s[i][j];j++)
            a[i][s[i][j]-'a']++;//统计每种字符的出现次数 
    }
    fo(i,n)
        ins(a[i],i);//插入每个出现次数数组 
    fo(i,n)
        f[i]=1;//每个字符串一开始都能选，所以f初始化为1 
    fo(i,n)
        fo1(j,0,25)//枚举每个添加的字符 
        {
            a[i][j]++;//在a数组里加上添加的字符，用于查找 
            t=fi(a[i]);//查找 
            a[i][j]--;//消除对a数组的影响 
            if(t&&f[t]<f[i]+1)//dp
            {
                f[t]=f[i]+1;
                p[t]=i;//记pre 
            }
        }
    fo(i,n)
        if(f[i]>mx)//找到最优解 
        {
            mx=f[i];
            ma=i;
        }
    _pn(mx);//输出答案，_pn就是输出并换行 
    op(ma);
}