#include <bits/stdc++.h>
#define P pair<int, int>
using namespace std;

inline int read(char c) {
    int a = 0;
    bool f = 0;
    while (!isdigit(c)) {
        if (c == '-')
            f = 1;
        c = getchar();
    }
    while (isdigit(c)) {
        a = (a << 3) + (a << 1) + (c ^ '0');
        c = getchar();
    }
    return f ? -a : a;
}

vector<P> Edge;

int main() {
    char c = getchar();
    int N = read(c), now = 0;
    if(c=='2'){
        printf("%d %d\n", 4, 5);
        printf("%d %d\n", 1, 2);
        printf("%d %d\n", 2, 1);
        printf("%d %d\n", 3, 4);
        printf("%d %d\n", 4, 3);
        printf("%d %d\n", 1, 4);
        return 0;
    }
    while (N) {
        int t = (1 + sqrt(8 * N + 1)) / 2 + 1e-8;
        if (now)
            Edge.push_back(P(now, now + 1));
        for (int i = now + 1; i < now + t; ++i) Edge.push_back(P(i, i + 1));
        Edge.push_back(P(now + t, now + 1));
        now += t;
        N -= t * (t - 1) / 2;
    }
    printf("%d %d\n", now, Edge.size());
    for (int i = 0; i < Edge.size(); ++i) printf("%d %d\n", Edge[i].first, Edge[i].second);
    return 0;
}

