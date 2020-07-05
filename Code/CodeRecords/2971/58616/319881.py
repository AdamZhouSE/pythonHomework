#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

const int N = 1000100;

char s[N];
int sa[N],t1[N],t2[N],c[N];
int n,m = 130;

void get_sa() {
    int *x = t1,*y = t2;
    for (int i=0; i<m; ++i) c[i] = 0;
    for (int i=0; i<n; ++i) c[x[i] = s[i]]++;
    for (int i=1; i<m; ++i) c[i] += c[i-1];
    for (int i=n-1; i>=0; --i) sa[--c[x[i]]] = i;
    for (int k=1; k<=n; k<<=1) {
        int p = 0;
        for (int i=n-k; i<n; ++i) y[p++] = i;
        for (int i=0; i<n; ++i) if (sa[i] >= k) y[p++] = sa[i] - k;
        for (int i=0; i<m; ++i) c[i] = 0;
        for (int i=0; i<n; ++i) c[x[y[i]]]++;
        for (int i=1; i<m; ++i) c[i] += c[i-1];
        for (int i=n-1; i>=0; --i) sa[--c[x[y[i]]]] = y[i];
        swap(x,y);
        p = 1;
        x[sa[0]] = 0;
        for (int i=1; i<n; ++i)
            x[sa[i]] = (y[sa[i-1]]==y[sa[i]] && sa[i-1]+k<n && sa[i]+k<n &&    
            y[sa[i-1]+k]==y[sa[i]+k]) ? p-1 : p++;       
        if (p >= n) break;
        m = p;
    }
}
int main() {
    scanf("%s",s);
    n = strlen(s);
    get_sa();
    for (int i=0; i<n; ++i) 
        printf("%d ",sa[i]+1);
    return 0;    
}