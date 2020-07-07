#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const int MM = 1e5 + 2;
int n, m, k, tail[MM], belong[MM];
vector<char> num[MM];
char ch;
bool visy[MM];
int belo[MM], ans;

struct node {
    int next, to;
} f[500020];

void maketo(int from, int to) {
    f[++k].to = to;
    f[k].next = tail[from];
    tail[from] = k;
}

bool dfs(int fa) {
    // cout<<"debug: "<<fa<<endl;
    //	for(register int i=tail[fa];i;i=f[i].next) if(belo[f[i].to]==0) belo[f[i].to]=2;
    for (register int i = tail[fa]; i; i = f[i].next) {
        int y = f[i].to;
        //		if(belo[y]!=2) continue;//表示是在左边
        if (!visy[y]) {
            visy[y] = true;
            if (!belong[y] || dfs(belong[y])) {
                belong[y] = fa;
                // cout<<"匹配: "<<y<<" "<<fa<<endl;
                return true;
            }
        }
    }
    return false;
}

void KM() {
    for (register int i = 1; i <= n * m; i++) {
        if (belo[i] == 0) {  //说明这个是左方 并且没有被探究过
            belo[i] = 1;     //标记是在左边
            if (dfs(i))
                ans++;
            memset(visy, 0, sizeof(visy));
        }
    }
    cout << ans << endl;
}

int main() {
    cin >> n >> m;

    for (register int i = 1; i <= n; i++)
        for (register int j = 1; j <= m; j++) {
            cin >> ch;
            num[i].push_back(ch);
        }
    for (register int i = 1; i <= n; i++) {
        for (register int j = 0; j < m; j++) {
            if (num[i][j] == '2') {
                ans++;
                belo[(i - 1) * m + j + 1] = 3;  //表示这个不参与
                continue;
            }
            if (num[i][j] == '*') {
                belo[(i - 1) * m + j + 1] = 3;
                continue;
            }
            if (i - 1 >= 1) {
                int x = num[i - 1][j] - '0', y = num[i][j] - '0';
                if (x + y == 4 && y == 3)
                    maketo((i - 1) * m + j + 1, (i - 2) * m + j + 1);
            }
            if (i + 1 <= n) {
                int x = num[i + 1][j] - '0', y = num[i][j] - '0';
                if (x + y == 4 && y == 3)
                    maketo((i - 1) * m + j + 1, (i)*m + j + 1);
            }
            if (j >= 1) {
                int x = num[i][j - 1] - '0', y = num[i][j] - '0';
                if (x + y == 4 && y == 3)
                    maketo((i - 1) * m + j + 1, (i - 1) * m + j);
            }
            if (j + 2 <= m) {
                int x = num[i][j + 1] - '0', y = num[i][j] - '0';
                if (x + y == 4 && y == 3)
                    maketo((i - 1) * m + j + 1, (i - 1) * m + j + 2);
            }
        }
    }
    KM();
    return 0;
}