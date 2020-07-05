#include<bits/stdc++.h>
#define read(a) a=getint()
using namespace std;
const int getint() {int x=0, f=1, c=getchar();for(;c<'0'||c>'9';c=getchar())if(c=='-') f=-1;for(;c>='0'&&c<='9';c=getchar()) x=x*10+c-48;return x*f;}
int n, k, ans, f;
struct node{int x, y;}a[50001];
bool cmp(node a,node b)
{return a.x+a.y<b.x+b.y;}
bool jud(node a,node b){
    return abs(a.x-b.x)<k && abs(a.y-b.y)<k;
}
int main() {
    read(n);read(k);
    for(int i=1;i<=n;++i) read(a[i].x),read(a[i].y);
    sort(a+1,a+n+1,cmp);
    for(int i=1; i<n; ++i) {
        int p = i + 1;
        while(a[i].x+a[i].y  + 2*k >= a[p].x+a[p].y && ans < 2 && p<=n) {
            if(jud(a[i],a[p])) ans ++, f = (k-abs(a[i].x-a[p].x))*(k-abs(a[i].y-a[p].y));
            p++;
        }
        if(ans>1) {puts("-1");return 0;}
    }
    if(ans) printf("%d\n",f);else puts("0");
    return 0;
}