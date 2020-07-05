#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 5, N = 1e5;

int x[maxn], y[maxn];
int que[maxn], tail,cnt;
bool vis[maxn];
int n, sum = 0;

int tree[maxn<<2], lazy[maxn<<2];

void pushup(int rt) {
    if (tree[rt<<1] == tree[rt<<1|1]) tree[rt] = tree[rt<<1];
    else if (!tree[rt<<1] || !tree[rt<<1|1]) tree[rt] = tree[rt<<1] + tree[rt<<1|1];
    else tree[rt] = -1;
}

void pushdown(int rt) {
    if (lazy[rt]) {
        tree[rt<<1] = tree[rt<<1|1] = lazy[rt];
        lazy[rt<<1] = lazy[rt<<1|1] = lazy[rt];
        lazy[rt] = 0;
    }
}

void query(int L, int R, int l, int r, int rt) {
    if (L <= l && r <= R && (~tree[rt])) { 
        if(tree[rt]) que[++tail] = tree[rt];
        return;
    }
    pushdown(rt);
    int mid=(l+r)>>1;
    if(L<=mid) query(L,R,l,mid,rt<<1);
    if(mid<R) query(L,R,mid+1,r,rt<<1|1);
    pushup(rt);
}

void update(int L, int R, int l, int r, int rt, int k) {
    if (L <= l && r<= R) {
        tree[rt] = lazy[rt] = k;
        return;
    }
    pushdown(rt);
    int mid=(l+r)>>1;
    if(L<=mid) update(L,R,l,mid,rt<<1,k);
    if(mid<R) update(L,R,mid+1,r,rt<<1|1,k);
    pushup(rt);
}


signed main() {
    cin>>n;
    string cmd;
    for (int i = 1; i <= n; i++) {
        cin>>cmd;
        if (cmd[0] == 'A') {
            cin>>x[i]>>y[i];
            tail = 0;
            query(x[i], y[i], 1, N, 1);
            cnt = 0;
            for (int j = 1; j <= tail; j++)
                if (!vis[que[j]]) { 
                    int s = x[que[j]], t = y[que[j]];
                    update(s,t,1,N,1,0);
                    vis[que[j]] = true;
                    cnt++;
                }
            update(x[i],y[i],1,N,1,i);
            cout<<cnt<<endl;
            sum = sum - cnt + 1;
        }
        else
            cout<<sum<<endl;
    }
    return 0;
}
