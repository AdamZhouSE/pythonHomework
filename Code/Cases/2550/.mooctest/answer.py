#include<iostream>
#include<cstdio>
#include<cmath>
#define maxn 100010
#define re register
#define FOR(i,l,r) for(re int i=l;i<=r;i++)
using namespace std;

int a[maxn],b[maxn],tag[maxn],ans[maxn];
int n,m,c,r,t,x,y,z,sq;

inline char nc(){  //快的一批的fread快读
    static char buf[100000],*p1=buf,*p2=buf; 
    return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++; 
}
inline int _read(){
    char ch=nc();
    int sum=0; 
    while(!(ch>='0'&&ch<='9'))ch=nc(); 
    while(ch>='0'&&ch<='9')sum=sum*10+ch-48,ch=nc(); 
    return sum; 
} 

inline void out(re int a){
    if(a>=10)out(a/10);
    putchar(a%10+'0');
}

void change(int x,int y){ //修改操作
    FOR(i,x,min(y,b[x]*sq)){//散块直接修改
        ans[b[x]]-=(a[i]^tag[b[x]]);  //维护ans数组
        a[i]^=1;
        ans[b[x]]+=(a[i]^tag[b[x]]);
    }
    if(b[x]!=b[y])
      FOR(i,(b[y]-1)*sq+1,y){
        ans[b[y]]-=(a[i]^tag[b[y]]);
        a[i]^=1;
        ans[b[y]]+=(a[i]^tag[b[y]]);
      }
    FOR(i,b[x]+1,b[y]-1){ //整块修改tag，维护ans数组
        tag[i]^=1;
        ans[i]=sq-ans[i];
    }
}

int query(int x,int y){ //查询操作
    re int res=0;
    FOR(i,x,min(y,b[x]*sq))  //散块直接查询
      res+=(a[i]^tag[b[x]]);
    if(b[x]!=b[y]) 
      FOR(i,(b[y]-1)*sq+1,y)
        res+=(a[i]^tag[b[y]]);
    FOR(i,b[x]+1,b[y]-1)
      res+=ans[i];  //整块加上维护的ans
    return res;
}

int main(){
    n=_read(),m=_read();
    sq=sqrt(n); //分块大小默认为根号n，修改也许能变得更快
    FOR(i,1,n)
      b[i]=(i-1)/sq+1; //每个点所在的块
    FOR(i,1,m){
        t=_read(),x=_read(),y=_read();
        if(t==0){
            change(x,y);
        }
        else{
            out(query(x,y));
            puts("");
        }
    }
    return 0;//功德圆满。
}