#include <bits/stdc++.h>

using namespace std;
const int N = 110, M = 1010;
int ver[M], Next[M], head[N], dfn[N], low[N];
stack<int> s;
bool ins[N];
int c[N], in[N], out[N];
vector<int> scc[N];
int n, tot, num, cnt;
int source, sink;

void add(int x, int y) {
    ver[++tot] = y;
    Next[tot] = head[x];
    head[x] = tot;
}

void read() {
    cin >> n;
    for (int x = 1; x <= n; x++) {
        int y;
        while (true) {
            scanf("%d", &y);
            if (!y)
                break;
            add(x, y);
        }
    }
}

void tarjain(int x) {
    dfn[x] = low[x] = ++num;
    s.push(x);
    ins[x] = true;
    for (int i = head[x]; i; i = Next[i])
        if (!dfn[ver[i]]) {
            tarjain(ver[i]);
            low[x] = min(low[x], low[ver[i]]);
        } else if (ins[ver[i]])
            low[x] = min(low[x], dfn[ver[i]]);
    if (dfn[x] == low[x]) {
        cnt++;
        int y;
        do {
            y = s.top();
            s.pop();
            ins[y] = false;
            c[y] = cnt;
            scc[cnt].push_back(y);
        } while (x != y);
    }
}

int main() {
    read();
    for (int i = 1; i <= n; i++)
        if (!dfn[i])
            tarjain(i);
    for (int x = 1; x <= n; x++)
        for (int i = head[x]; i; i = Next[i]) {
            int y = ver[i];
            if (c[x] == c[y])
                continue;
            out[c[x]]++;
            in[c[y]]++;
        }
    for (int i = 1; i <= cnt; i++) {
        if (!in[i])
            source++;
        if (!out[i])
            sink++;
    }
    cout << source << endl;
    if (cnt == 1)
        cout << 0;
    else{
        cout << max(sink, source);
    }
    cout<<'\n';
    return 0;
}
