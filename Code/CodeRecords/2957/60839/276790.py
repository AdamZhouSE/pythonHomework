#include <bits/stdc++.h>
using namespace std;
template <typename T> void read(T &t) {
    char ch=getchar(); int f=1; t=0;
    while ('0'>ch||ch>'9') { if (ch=='-') f=-1; ch=getchar(); }
    do { (t*=10)+=ch-'0'; ch=getchar(); } while ('0'<=ch&&ch<='9'); t*=f;
}
typedef long long ll;
const int maxn=200010;
int n,c1,c2,a[30];
ll ans;
map<pair<int,int>,int> b[30];
struct node {
    int k1,k2,c1,c2;
} d[maxn];
char s[maxn],k1,k2;
int main() {
    scanf("%s",s+1); n=strlen(s+1);
    int pos=0,cnt=0; s[0]=s[1];
    for (int i=1;i<=n;i++) {
        while (pos<n) {
            if (s[pos]!=s[pos+1]&&cnt==1) break;
            if (s[pos]!=s[pos+1]) {
                cnt++;
                k2=s[pos+1]; c2++;
            } else if (c2) c2++; else k1=s[pos],c1++;
            pos++;
        }
        d[i]=(node){k1-'a'+1,k2-'a'+1,c1,c2};
        a[k1-'a'+1]=max(a[k1-'a'+1],c1);
        if (s[i]!=s[i+1]) {
            cnt--;
            k1=k2; c1=c2; c2=0;
        } else c1--;
    }
    for (int i=1;i<=26;i++)
        ans+=a[i];
    for (int i=1;i<=n;i++) {
        if (d[i].c2==0) continue;
        int tmp=b[d[i].k1][make_pair(d[i].c1,d[i].k2)];
        b[d[i].k1][make_pair(d[i].c1,d[i].k2)]=max(tmp,d[i].c2);
        ans+=max(0,d[i].c2-tmp);
    }
    printf("%lld\n",ans);
    return 0;
}
