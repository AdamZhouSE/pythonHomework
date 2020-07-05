#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#define MAXN 400010
using namespace std;
pair<int,long long> stack[MAXN];
int n,l1,l2;
int val[MAXN],sum[MAXN];
char str[MAXN];
int top,sa[MAXN],rk[MAXN],tax[MAXN],tp[MAXN],height[MAXN];
inline int read(){
    int date=0,w=1;char c=0;
    while(c<'0'||c>'9'){if(c=='-')w=-1;c=getchar();}
    while(c>='0'&&c<='9'){date=date*10+c-'0';c=getchar();}
    return date*w;
}
void radixsort(){
    for(int i=0;i<=top;i++)tax[i]=0;
    for(int i=1;i<=n;i++)tax[rk[i]]++;
    for(int i=1;i<=top;i++)tax[i]+=tax[i-1];
    for(int i=n;i>=1;i--)sa[tax[rk[tp[i]]]--]=tp[i];
}
void suffixsort(){
    top=30;
    for(int i=1;i<=n;i++){
        rk[i]=val[i];
        tp[i]=i;
    }
    radixsort();
    for(int w=1,p=0;p<n;top=p,w<<=1){
        p=0;
        for(int i=1;i<=w;i++)tp[++p]=n-w+i;
        for(int i=1;i<=n;i++)if(sa[i]>w)tp[++p]=sa[i]-w;
        radixsort();
        swap(tp,rk);
        rk[sa[1]]=p=1;
        for(int i=2;i<=n;i++)
        rk[sa[i]]=(tp[sa[i-1]]==tp[sa[i]]&&tp[sa[i-1]+w]==tp[sa[i]+w])?p:++p;
    }
}
void getheight(){
    for(int i=1,j,k=0;i<=n;i++){
        if(k)k--;
        j=sa[rk[i]-1];
        while(val[i+k]==val[j+k])k++;
        height[rk[i]]=k;
    }
}
void work(){
    long long ans=0;
    top=0;
    stack[0]=make_pair(1,0);
    for(int i=1;i<=n;i++)sum[i]=sum[i-1]+(sa[i]<=l1);
    for(int i=1;i<=n;i++){
        while(top&&height[i]<height[stack[top].first])top--;
        top++;
        stack[top]=make_pair(i,(long long)(sum[i-1]-sum[stack[top-1].first-1])*height[i]+stack[top-1].second);
        if(sa[i]>l1+1)ans+=stack[top].second;
    }
    top=0;
    for(int i=1;i<=n;i++)sum[i]=sum[i-1]+(sa[i]>l1+1);
    for(int i=1;i<=n;i++){
        while(top&&height[i]<height[stack[top].first])top--;
        top++;
        stack[top]=make_pair(i,(long long)(sum[i-1]-sum[stack[top-1].first-1])*height[i]+stack[top-1].second);
        if(sa[i]<=l1+1)ans+=stack[top].second;
    }
    printf("%lld\n",ans);
}
void init(){
    scanf("%s",str+1);
    l1=n=strlen(str+1);
    str[++n]='z'+1;
    scanf("%s",str+n+1);
    n=strlen(str+1);
    for(int i=1;i<=n;i++)val[i]=str[i]-'a'+1;
    suffixsort();
    getheight();
}
int main(){
    init();
    work();
    return 0;
}

