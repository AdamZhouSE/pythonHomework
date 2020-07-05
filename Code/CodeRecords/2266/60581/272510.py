
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
typedef unsigned long long LL;

const int MAXN = 1e5 + 5, MAXT = 1e7 + 5;
const LL Pri = 99877171;

struct HashList {LL Num; int New;} Map[MAXT];
struct Info {
    int Num, Poi;
    Info (void) {};
    Info (int A, int B) {Num = A, Poi = B;};
};

vector<Info> Son[MAXN];
vector<LL> Suf[MAXN];

LL State[MAXN], Pow[MAXN], Hash[MAXN];
int Cnt, N, Real[MAXN], Siz[MAXN], tot, Next[MAXN * 2], Go[MAXN * 2], Last[MAXN];
bool Exist[MAXT];

int Get(LL Sta) {
    int Now = Sta % MAXT;
    while (Map[Now].New != 0 && Map[Now].Num != Sta) Now = (Now + 1) % MAXT;
    if (!Map[Now].New) Map[Now].New = ++ Cnt, Map[Now].Num = Sta;
    return Map[Now].New;
}

void Link(int u, int v) {
    Next[++ tot] = Last[u], Last[u] = tot, Go[tot] = v;
}

bool Cmp(Info A, Info B) {return A.Num < B.Num;}

void Basis(int Now, int Pre) {
    for (int p = Last[Now]; p; p = Next[p]) {
        int v = Go[p];
        if (v == Pre) continue;
        Basis(v, Now);
        Son[Now].push_back(Info(Hash[v], v));
    }
    sort(Son[Now].begin(), Son[Now].end(), Cmp);
    int Size = Son[Now].size();
    LL Sta = 0;
    for (int i = 0; i < Size; i ++) 
        Sta = Sta * Pri + Son[Now][i].Num;
    Hash[Now] = Get(Sta);
}

void All(int Now, int Pre, LL PreS) {
    LL Sta = 0;
    if (Now != 1) Son[Now].push_back(Info(PreS, Pre));
    int Size = Son[Now].size();
    sort(Son[Now].begin(), Son[Now].end(), Cmp);
    for (int i = 0; i < Size; i ++) 
        Sta = Sta * Pri + Son[Now][i].Num;
    State[Now] = Sta, Siz[Now] = Size;
    Real[Now] = Get(Sta);
    Suf[Now].clear();
    Suf[Now].resize(Size + 1);
    for (int i = Size - 1, j = 0; i + 1; i --, j ++) 
        Suf[Now][i] = Suf[Now][i + 1] + Pow[j] * Son[Now][i].Num;
    LL Pref = 0;
    for (int i = 0; i < Size; i ++) {
        Info v = Son[Now][i];
        if (i) Pref = Pref * Pri + Son[Now][i - 1].Num;
        if (v.Poi == Pre) continue;
        int Num = Suf[Now][i + 1];
        All(v.Poi, Now, Get(Pref * Pow[Size - i - 1] + Suf[Now][i + 1]));
    }
}

void Solve(int Ord) {
    Basis(1, 0);
    All(1, 0, 0);
    if (Ord == 1) {
        for (int i = 1; i <= N; i ++) Exist[Real[i]] = 1;
        return;
    }
    if (!Next[Last[1]]) {
        int Now = Go[Last[1]];
        if (Exist[Get(State[Now] - Pow[Siz[Now] - 1])]) {
            printf("1");
            return;
        }
    }
    for (int i = 2; i <= N + 1; i ++) {
        if (Next[Last[i]]) continue;
        int Now = Go[Last[i]];
        if (!Exist[Get(State[Now] - Pow[Siz[Now] - 1])]) continue;
        printf("%d", i);
        return;
    }
}

void Prepare() {
    Pow[0] = 1;
    for (int i = 1; i <= N + 1; i ++) Pow[i] = Pow[i - 1] * Pri;
}

void Clear() {
    tot = 0;
    memset(Last, 0, sizeof Last);
    memset(Son, 0, sizeof Son);
    memset(Hash, 0, sizeof Hash);
}

int main() {
    scanf("%d", &N);
    Prepare();
    for (int i = 1; i < N; i ++) {
        int u, v;
        scanf("%d%d", &u, &v);
        Link(u, v), Link(v, u);
    }
    Solve(1);
    Clear();
    for (int i = 1; i <= N; i ++) {
        int u, v;
        scanf("%d%d", &u, &v);
        Link(u, v), Link(v, u);
    }
    Solve(2);
}