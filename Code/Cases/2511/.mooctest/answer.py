#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#define LL long long
#define Re register int
using namespace std;
const int N=1e5+5;
int n,s,a[N];LL S[N];
inline void in(Re &x){
    int f=0;x=0;char c=getchar();
    while(c<'0'||c>'9')f|=c=='-',c=getchar();
    while(c>='0'&&c<='9')x=(x<<1)+(x<<3)+(c^48),c=getchar();
    x=f?-x:x;
}
inline int judge1(Re i,Re mid){return S[mid]-S[i-1]<=s;}
//judge1()判断序列前半段
inline int judge2(Re i,Re mid){return S[(mid<<1)-i+1]-S[mid]<=s;}
//judge2()判断序列前半段
int main(){
//  freopen("b.in","r",stdin);
//  freopen("b.out","w",stdout);
    in(n),in(s);
    for(Re i=1;i<=n;++i)in(a[i]),S[i]=S[i-1]+a[i];
    Re p=0;S[n+1]=S[n+2]=1e18;//为防止玄学错误，先把最后面的覆盖一下
    while((p+1<<1)<=n&&judge1(1,p+1))++p;//预处理出第一个mid
    while(p&&!judge2(1,p))--p;
    printf("%d\n",(p<<1));
    for(Re i=2;i<=n;++i){
//      if(p<i-1)p=i-1;//这句可加可不加
        while((p+1<<1)-i+1<=n&&judge1(i,p+1))++p;//向后移时注意判断右边界不能超过n
        while(p>=i&&!judge2(i,p))--p;//向前移回去，找到最大的合法mid_i
        printf("%d\n",(p-i+1)<<1);//输出为长度
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}