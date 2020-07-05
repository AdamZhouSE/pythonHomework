#include<cstdio>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#define For(i,x,y) for (int i=(x);i<=(y);i++)
#define Dow(i,x,y) for (int i=(x);i>=(y);i--)
#define cross(i,k) for (int i=first[k];i;i=last[i])
#define il inline
#define vd void
#define ll long long
#define N 2000010
using namespace std;
namespace fast_IO {
    inline char read() {
        return getchar();
        static const int IN_LEN = 1000000;
        static char buf[IN_LEN], *s, *t;
        if (s == t) {
            t = (s = buf) + fread(buf, 1, IN_LEN, stdin);
            if (s == t) return -1;
        }
        return *s++;
    }
    template<class T>
    inline void read(T &x) {
        static bool iosig;
        static char c;
        for (iosig = false, c = read(); !isdigit(c); c = read()) {
            if (c == '-') iosig = true;
            if (c == -1) return;
        }
        for (x = 0; isdigit(c); c = read())
            x = ((x + (x << 2)) << 1) + (c ^ '0');
        if (iosig) x = -x;
    }
    const int OUT_LEN = 10000000;
    char obuf[OUT_LEN], *ooh = obuf;
    inline void print(char c) {
        if (ooh == obuf + OUT_LEN) fwrite(obuf, 1, OUT_LEN, stdout), ooh = obuf;
        *ooh++ = c;
    }
    template<class T>
    inline void print(T x) {
        static int buf[30], cnt;
        if (x == 0) {
            print('0');
        }
        else {
            if (x < 0) print('-'), x = -x;
            for (cnt = 0; x; x /= 10) buf[++cnt] = x % 10 + 48;
            while (cnt) print((char)buf[cnt--]);
        }
    }
    inline void flush() {
        fwrite(obuf, 1, ooh - obuf, stdout);
    }
}
using namespace fast_IO;
struct node{
    int l,r,id;
}q[N];
int c[N],ans[N],n,m,k,color[N],first[N],next[N],nnext[N],b[N];
il bool cmp(node x,node y){return x.l<y.l;}
il int lowbit(int x){return x&(-x);}
il vd add(int x,int y){
    for(int i=x;i<=n;i+=lowbit(i)) c[i]+=y;
}
il int query(int x){
    int sum=0;
    for (int i=x;i>0;i-=lowbit(i)) sum+=c[i];
    return sum;
}
int main(){
    read(n),read(k),read(m);
    For(i,1,n) read(color[i]);
    Dow(i,n,1){
        next[i]=first[color[i]];
        first[color[i]]=i;
    }
    For(i,1,n)
        nnext[i]=next[next[i]];
    For(i,1,n)
        if (++b[color[i]]==2) add(i,1);
    For(i,1,m){
        read(q[i].l),read(q[i].r);
        q[i].id=i;
    }
    sort(q+1,q+1+m,cmp);
    int now=1;
    For(i,1,m){
        for (;now<q[i].l;now++){
            if (next[now]) add(next[now],-1);
            if (nnext[now]) add(nnext[now],1);
        }
        ans[q[i].id]=query(q[i].r)-query(q[i].l-1);
    }
    For(i,1,m) print(ans[i]),print('\n');
    flush();
}