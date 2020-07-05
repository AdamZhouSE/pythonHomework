#include<bits/stdc++.h>
using namespace std;
const int maxn=200005;
int n,cnt,a[maxn],mn=9999999,gett[maxn];   
inline int read_d(){
    int s=0;
    char c;
    while(c=getchar(),c<'0'||c>'9');
    while(c<='9'&&c>='0') {
        s=s*10+c-'0';
        c=getchar();
    }
    return s;
}
inline void dfs(int x){
    if(a[x]==0) return;
    cnt++;
    if(cnt>gett[x] && gett[x]){
        mn=min(cnt-gett[x],mn);
        cnt=0;
        a[x]=0;
        return;
    }
    gett[x]=cnt;
    dfs(a[x]);
    gett[x]=0;
    a[x]=0;
}
int main(){
    n=read_d();
    for(register int i=1;i<=n;i++){
        int x;
        x=read_d();
        a[i]=x;
    }
    for(register int i=1;i<=n;i++)  dfs(a[i]);
    printf("%d",mn);
    return 0;
}