#include<iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define maxn 200010
#define re register
#define FOR(i, l, r) for(re int i = l; i <= r; ++i)
using namespace std;

int n, m, c, r, x, y, z, k;
int sq;
int a[maxn], b[maxn], minn[2002];
char t;

inline void in(re int &x){
    x=0;int bl = 1;char c=getchar();
    while(c<'0'||c>'9'){
        if(c == '-')
          bl = -1;
        c=getchar();
    }
    while(c<='9'&&c>='0'){
        x=(x<<1)+(x<<3)+(c^'0');
        c=getchar();
    }
    x *= bl;
}

void out(re int a){
    if(a < 0) {
        putchar('-');
        a = -a;
    }
    if(a>=10)out(a/10);
    putchar(a%10+'0');
}

inline int query(int x, int y, int k) {
    FOR(i, x, min(y, b[x]*sq)) 
      if(a[i] <= k)
        return i;
    FOR(i, b[x]+1, b[y]-1) { 
        if(minn[i] > k) 
          continue;
        FOR(j, (i-1)*sq+1, i*sq) 
          if(a[j] <= k)
            return j; 
    }   
    if(b[x] != b[y]) 
      FOR(i, (b[y]-1)*sq+1, y)
        if(a[i] <= k)
          return i;
    return -1;
}

int main(){
    in(n), in(m);
    sq = sqrt(n);
    FOR(i, 1, sq+100)
      minn[i] = 0x7fffffff;
    FOR(i, 1, n)
      a[i] = 0x7fffffff, b[i] = (i-1)/sq+1, minn[b[i]] = min(minn[b[i]], a[i]);
    FOR(i, 1, m) {
        cin >> t;
        if(t == 'M') {
            in(x), in(y); 
            a[y] = x;
            minn[b[y]] = min(minn[b[y]], x); 
        }
        else {
            in(k), in(x);
            out(query(x, n, k));
            putchar(10);
        }
    }

} 