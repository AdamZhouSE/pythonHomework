#include <bits/stdc++.h>
using namespace std;
char s[15];
int ch[1100][2], f[1100], tot = 1, flag = 0, t;
void zds() {
    int len = strlen(s);
    int u = 1;
    for (int i = 0; i < len; i++) {
        int c = s[i] - '0';
        if (!ch[u][c])
            ch[u][c] = ++tot;
        else if (i == len - 1)
            flag = 1;
        u = ch[u][c];
        if (f[u])
            flag = 1;
    }
    f[u] = 1;
}
int main() {
    while (scanf("%s", s) != EOF) {
        t++;
        memset(ch, 0, sizeof(ch));
        // tot=1;
        zds();
        while (scanf("%s", s)) {
            if (s[0] == '9')
                break;
            zds();
        }
        if (flag)
            cout << "Set " << t << " is not immediately decodable" << endl;
        else
            cout << "Set " << t << " is immediately decodable" << endl;
        flag = 0;
    }
    return 0;
}