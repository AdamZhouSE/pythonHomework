
#include<iostream>

#include<cstdio>

#include<cmath>

#include<cstring>

#include<algorithm>

#define LL long long int

#define Redge(u) for (int k = h[u],to; k; k = ed[k].nxt)

#define REP(i,n) for (int i = 1; i <= (n); i++)

#define BUG(s,n) for (int i = 1; i <= (n); i++) cout<<s[i]<<' '; puts("");

using namespace std;

const int maxn = 13,maxm = 10000,INF = 1000000000;

inline int read(){

    int out = 0,flag = 1; char c = getchar();

    while (c < 48 || c > 57){if (c == '-') flag = -1; c = getchar();}

    while (c >= 48 && c <= 57){out = (out << 3) + (out << 1) + c - 48; c = getchar();}

    return out * flag;

}

int a[maxm],n,N,chs;

LL ans,fac[maxn];

bool isorder(int l,int len){

    for (int i = 1; i < len; i++) if (a[l + i] != a[l + i - 1] + 1) return false;

    return true;

}

void Swap(int u,int v,int len){

    for (int i = 0; i < len; i++) swap(a[u + i],a[v + i]);

}

void dfs(int dep){

    if (dep > n){

        if (isorder(1,N)) ans += fac[chs];

        return;

    }

    int len = 1 << dep,x = 0,y = 0;

    for (int i = 1; i <= N; i += len){

        if (!isorder(i,len)){

            if (!x) x = i;

            else if (!y) y = i;

            else return;

        }

    }

    if (!x && !y) dfs(dep + 1);

    else if (x && !y){

        chs++;

        Swap(x,x + (len >> 1),(len >> 1));

        dfs(dep + 1);

        Swap(x,x + (len >> 1),(len >> 1));

        chs--;

    }

    else if (x && y){

        chs++;

        for (int i = 0; i < 2; i++)

            for (int j = 0; j < 2; j++){

                Swap(x + i * (len >> 1),y + j * (len >> 1),(len >> 1));

                if (isorder(x,len) && isorder(y,len))

                    dfs(dep + 1);

                Swap(x + i * (len >> 1),y + j * (len >> 1),(len >> 1));

        }

        chs--;

    }

}

int main(){

    fac[0] = 1;

    for (int i = 1; i <= 12; i++) fac[i] = fac[i - 1] * i;

    n = read(); N = (1 << n);

    REP(i,N) a[i] = read();

    dfs(1);

    cout << ans << endl;

    return 0;

}