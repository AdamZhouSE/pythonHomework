#include<bits/stdc++.h>
using namespace std;
int t,n,a[600010];
#define li long long
#define gc getchar()
#define pc putchar
int read(){
    int x = 0,c = gc;
    while(!isdigit(c)) c = gc;
    while(isdigit(c)){
        x = (x << 1) + (x << 3) + (c ^ '0');
        c = gc;
    }
    return x;
}
void print(int x){
    if(x >= 10) print(x / 10);
    pc(x % 10 + '0');
}
int tt[1200010];
void xg(int q){
    for(int i = q;i <= n;i += i & (-i)) ++tt[i];
}
int cx(int q){
    int as = 0;
    for(int i = q;i;i -= i & (-i)) as += tt[i];
    return as;
}
int b[600010],c[600010];
li jc[1200010],nj[1200010];
const int mo = 998244353;
li ksm(li q,li w){
    li as = 1;
    while(w){
        if(w & 1) as = as * q % mo;
        q = q * q % mo;
        w >>= 1;
    }
    return as;
}
int mx1 = 1200005;
inline li zh(li q,li w){
    return jc[q] * nj[w] % mo * nj[q - w] % mo;
}
inline li wk(li q,li w){
    if(w == 0) return 1;
    if(w == 1) return q;
    return (zh(q + w - 1,w) - zh(q + w - 1,w - 2) + mo) % mo;
}
int main(){
    int i,j;
    jc[0] = 1;
    for(i = 1;i <= mx1;++i) jc[i] = jc[i - 1] * i % mo;
    nj[mx1] = ksm(jc[mx1],mo - 2);
    for(i = mx1 - 1;i >= 0;--i) nj[i] = nj[i + 1] * (i + 1) % mo;
    t = read();
    while(t--){
        n = read();
        for(i = 1;i <= n;++i) a[i] = read(),tt[i] = 0;
        for(i = n;i;--i){
            b[i] = n - i - cx(a[i]);
            xg(a[i]);
            c[i] = i - 1 - (n - a[i] - b[i]);

        }
        li as = 0;int nw = n; 
        for(i = 1;i <= n;++i){
            bool fg = b[i] < nw;
            nw = min(nw,b[i]);
            if(nw <= 0) break;
            (as += wk(n - i + 1,nw - 1)) %= mo;
            if(!fg && c[i] != a[i] - 1) break;
        } 
        print(as);pc('\n');
    } 
    return 0;
}