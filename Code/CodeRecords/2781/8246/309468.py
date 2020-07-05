#include <iostream>
#include <cstdio>
#include <cstring>
#define N 1005
using namespace std;
int ch[N][2], tag[N], cnt, ans, cas;
char str[N];
int idx(char x) { return x - '0'; }
void insert() {
    int u = 0, len = strlen(str + 1), r = 1;
    for (int i = 1; i <= len; i++) {
        int v = idx(str[i]);
        if (!ch[u][v])
            ch[u][v] = ++cnt, r = 0;
        if (tag[u])
            ans = 1;
        u = ch[u][v];
    }
    tag[u] = 1;
    if (r == 1)
        ans = 1;
}
int main() {
    while (scanf("%s", str + 1) != EOF) {
        if (str[1] == '9') {
            if (!ans)
                printf("Set %d is immediately decodable\n", ++cas);
            else
                printf("Set %d is not immediately decodable\n", ++cas);
            cnt = 0;
            ans = 0;
            memset(ch, 0, sizeof(ch));
            memset(tag, 0, sizeof(tag));
        } else {
            insert();
        }
    }
}