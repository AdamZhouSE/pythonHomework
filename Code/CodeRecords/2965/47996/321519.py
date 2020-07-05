#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fod(i,a,b) for(i=a;i>=b;i--)
using namespace std;
const int maxn=200007;
int i,j,k,l,t,n,m,ans;
char s[10000000];
int a[maxn],b[maxn],c[maxn];
int main(){
    scanf("%d%d",&k,&m);
    scanf("%s",s+1);
    n=strlen(s+1);
    scanf("%d",&l);
    fo(i,1,l){
        scanf("%d%d%d",&a[i],&b[i],&c[i]);
        a[i]++;c[i]++;
    }
    fo(i,1,k){
        t=i;
        fod(j,l,1){
            if(c[j]<=t&&t<=c[j]+b[j]-a[j]){
                t=a[j]+(t-c[j]);
            } else if (c[j]+b[j]-a[j]<t)t-=(b[j]-a[j]+1);
        }
        putchar(s[t]);
    }
}