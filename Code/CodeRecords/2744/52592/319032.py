#include <cstdio>
#include <cstring>
#include <string>
const int MO = 1e9 + 7, base = 255;
int ch[2000005][26], tot = 1;
int wrd[2000005], cnt[2000005];
int n, len[2000005], hash[2000005], bpow[2000005];
std::string str[2000005];
char strt[2000005];
long long ans = 0;
inline void insert(char* str, int id) {
    int t = 1;
    for(int i = 0; i < len[id]; i++) {
        if(!ch[t][str[i] - 'a']) {
            t = ch[t][str[i] - 'a'] = ++tot;
        } else {
            t = ch[t][str[i] - 'a'];
        }
    }
    wrd[t] = id;
    cnt[t]++;
}

inline int calhash(char* str, int len) {
    long long res = 0;
    for(int i = 0; i < len; i++) {
        res = (res * base + str[i]) % MO;
    }
    return res;
}

int main() {
    scanf("%d", &n);
    bpow[0] = 1;
    for(int i = 1; i < 2000005; i++) {
        bpow[i] = (1ll * bpow[i - 1] * base) % MO;
    }
    for(int i = 1; i <= n; i++) {
        scanf("%d%s", &len[i], strt);
        insert(strt, i);
        hash[i] = calhash(strt, len[i]);
        str[i] = strt;
    }
    for(int i = 1; i <= n; i++) {
        int u = 1;
        for(int j = 0; j < len[i]; j++) {
            u = ch[u][str[i][j] - 'a'];
            if(wrd[u]) {
                if((1ll * hash[wrd[u]] * bpow[len[i]] % MO + hash[i]) % MO == (1ll * hash[i] * bpow[len[wrd[u]]] % MO + hash[wrd[u]]) % MO) {
                    ans = ans + 1ll * cnt[u] * 2;
                }
            }
        }
    }
    printf("%lld", ans - n);
    printf("\n");
    return 0;
}