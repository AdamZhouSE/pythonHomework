#include <bits/stdc++.h>
using namespace std;
#define reg register
int n, ans;
char str[30005][3005];
bool can[30005], cant[300005];
bool appear[300005][27];
int nxt[300005][27], tot, dep[300005], End[300005];
inline void Insert(char *s)
{
    int len = strlen(s + 1);
    int now = 0;
    for (reg int i = 1 ; i <= len ; i ++)
    {
        if (!nxt[now][s[i]-'a']) nxt[now][s[i]-'a'] = ++tot, dep[nxt[now][s[i]-'a']] = dep[now] + 1;
        now = nxt[now][s[i]-'a'];
        appear[dep[now]][s[i]-'a'] = 1;
    }
    End[now] = 1;
}

void dfs(int x, bool ap) 
{
    if (ap) cant[x] = 1;
    for (reg int i = 0 ; i <= 25 ; i ++)
        if (nxt[x][i]) dfs(nxt[x][i], ap | End[x]);
}

vector <int> ve[27];
int deg[27];
bool ex[27][27];

inline bool Topsort()
{
    queue <int> q;
    for (reg int i = 0 ; i <= 25 ; i ++) if (!deg[i]) q.push(i);
    while(!q.empty())
    {
        int x = q.front();q.pop();
        for (reg int i = 0 ; i < ve[x].size() ; i ++) 
        {
            int to = ve[x][i];
            deg[to]--;
            if (!deg[to]) q.push(to);
        }
    }
    for (reg int i = 0 ; i <= 25 ; i ++)
        if (deg[i]) return 0;
    return 1;
}

inline bool Build(int id)
{
    for (reg int i = 0 ; i <= 25 ; i ++) ve[i].clear(), deg[i] = 0;
    int len = strlen(str[id] + 1);
    int now = 0;
    for (reg int i = 1 ; i <= len ; i ++)
    {
        for (reg int j = 'a' ; j <= 'z' ; j ++) 
        {
            if (!nxt[now][j-'a'] or j == str[id][i]) continue;
            ve[j-'a'].push_back(str[id][i]-'a');
            deg[str[id][i]-'a']++;
//            printf("%c -> %c\n", j, str[id][i]);
        }
        now = nxt[now][str[id][i]-'a'];
        if (cant[now]) return 0;
    }
    return Topsort();
}


int main()
{
    scanf("%d", &n);
    for (reg int i = 1 ; i <= n ; i ++)
    {
        scanf("%s", str[i] + 1);
        Insert(str[i]);
    }
    dfs(0, 0);
    for (reg int i = 1 ; i <= n ; i ++)
    {
        can[i] = Build(i);
        ans += can[i];
//        printf("%d %d\n", i, can[i]);
    }
    cout << ans << endl;
    for (reg int i = 1 ; i <= n ; i ++)
        if (can[i]) {
            int len = strlen(str[i] + 1);
            for (reg int j = 1 ; j <= len ; j ++) printf("%c", str[i][j]);
            puts("");
        }
    return 0;
}