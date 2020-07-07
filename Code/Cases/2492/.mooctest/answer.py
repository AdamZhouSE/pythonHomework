#include <bits/stdc++.h>

using namespace std;

#define N 503

struct node{
    int x, y;
}le[N], cz[N];
int m[N], cnt;
int n, E;

bool cmp1 (node a, node b) {
    return a.x == b.x ? a.y < b.y : a.x < b.x;
}
bool cmp2 (node a, node b) {
    return a.y == b.y ? a.x < b.x : a.y < b.y;
}

int getcnt(int l, int a) {
    int r = l + a - 1;
    cnt = 0;
    for(int i = 1; i <= n; ++i) { //处理m
        if(cz[i].x <= r && cz[i].x >= l)
            m[++cnt] = cz[i].y;
    }
    int p1 = 1, p2 = 1;
    while(m[p2] - m[p1] + 1 <= a && p2 <= cnt) ++p2;  //滚动p2
    if(p2 > cnt || m[p2] - m[p1] + 1 > a) --p2;
    //一定要注意这里！指针有可能滚过头了，还要让她滚回来！！！
    int ans = 0;
    while(p1 <= p2 && p2 <= cnt) {
        ans = max(ans, p2 - p1 + 1); //p2 - p1 + 1就是包含的点数
        ++p2;
        while(m[p2] - m[p1] + 1 > a) ++p1; //根据p2滚动p1
    }
    return ans;
}

bool check(int mid) { //枚举每一个点并求出[L, L + mid]的最大点数
    for(int i = 1; i <= n; ++i) {
        if(getcnt(le[i].x, mid) >= E) {
            return true;
        }
    }
    return false;
}

int erfen(int l, int r) { //二分答案
    if(l == r) return l;
    int mid = l + r >> 1;
    if(check(mid)) erfen(l, mid);
    else erfen(mid + 1, r);
} 

int main() {
    scanf("%d%d", &E, &n);
    for(int i = 1; i <= n; ++i) 
        scanf("%d%d", &le[i].x, &le[i].y), 
          cz[i].x = le[i].x, cz[i].y = le[i].y;
    sort(le + 1, le + n + 1, cmp1); //横坐标第一关键字排序
    sort(cz + 1, cz + n + 1, cmp2); //纵坐标第一关键字排序
    int ans = erfen(1, 10003);
    printf("%d\n", ans);
    return 0;
}