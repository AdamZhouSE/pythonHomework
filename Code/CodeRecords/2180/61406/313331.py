#include<bits/stdc++.h>
using namespace std;
const int N = 4e5+5;
typedef int _int;
#define int long long

int n, m, l1, l2, L[N], R[N], stk[N], top = 0, ans = 0;
int sa[N], rk[N], sec[N], buk[N], height[N];
char s1[N], s2[N], s[N];

void rsort(){
    for(int i = 0; i <= m; i++) buk[i] = 0;
    for(int i = 1; i <= n; i++) buk[rk[i]]++;
    for(int i = 1; i <= m; i++) buk[i] += buk[i-1];
    for(int i = n; i >= 1; i--) sa[buk[rk[sec[i]]]--] = sec[i];
}

void SuffixArray(){
    for(int i = 1; i <= n; i++) rk[i] = s[i], sec[i] = i;
    int cnt = 0; m = 300, rsort();
    for(int l = 1; l <= n && cnt < n; l <<= 1){
        cnt = 0;
        for(int i = 1; i <= l; i++) sec[++cnt] = n-l+i;
        for(int i = 1; i <= n; i++) if(sa[i] > l) sec[++cnt] = sa[i]-l;
        rsort(); swap(sec, rk), rk[sa[1]] = cnt = 1;
        for(int i = 2; i <= n; i++)
            rk[sa[i]] = (sec[sa[i]] == sec[sa[i-1]] && sec[sa[i]+l] == sec[sa[i-1]+l]) ? cnt : ++cnt;
        m = cnt;
    }
}

void get_height(){
    int j, k = 0;
    for(int i = 1; i <= n; i++){
        if(k) k--;
        j = sa[rk[i]-1];
        while(s[i+k] == s[j+k]) k++;
        height[rk[i]] = k;
    }
}

int solve(){
    memset(L, 0, sizeof(L)), memset(R, 0, sizeof(R));
    memset(sa, 0, sizeof(sa)), memset(rk, 0, sizeof(rk));
    memset(height, 0, sizeof(height));
    memset(sec, 0, sizeof(sec));
    SuffixArray(), get_height();
    int res = 0; stk[top = 0] = 1;
    for(int i = 2; i <= n; i++){
        while(top && height[stk[top]] >= height[i]) top--;
        L[i] = stk[top], stk[++top] = i;
    }
    stk[top = 0] = n+1;
    for(int i = n; i >= 2; i--){
        while(top && height[stk[top]] > height[i]) top--;
        R[i] = stk[top], stk[++top] = i;
    }
    for(int i = 2; i <= n; i++) res += height[i]*(i-L[i])*(R[i]-i);
    return res;
}

_int main(){
    scanf("%s%s", s1+1, s2+1), l1 = strlen(s1+1), l2 = strlen(s2+1);
    for(int i = 1; i <= l2; i++) s[i] = s2[i];
    n = l2; ans -= solve();
    for(int i = 1; i <= l1; i++) s[i] = s1[i];
    n = l1; ans -= solve();
    for(int i = 1; i <= l2; i++) s[i+l1+1] = s2[i];
    s[l1+1] = '#', n = l1+l2+1; ans += solve();
    cout << ans;
    return 0;
}