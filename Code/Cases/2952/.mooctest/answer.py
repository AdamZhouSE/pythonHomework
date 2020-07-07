#include <cstdio>
#include <queue>
#include <cstring>
#include <vector>
const int MaxN = 1e5 + 10;

struct Trie {
    int Vis[30], End, Fail, Fa;
}Ac[MaxN];
int P = 1;

struct Edge {
    int To, Next;
}Road[MaxN];

struct Query {
    int X, Y;
};
int Last[MaxN], Cnt;

void Add(int U, int V) {
    Road[++Cnt] = (Edge) {V, Last[U]}, Last[U] = Cnt;
}

int Lowbit(int X) {
    return X & (-X);
}

int Tree[MaxN];
int N, M;

void Update(int X, int K) {
    while(X < MaxN) {
        Tree[X] += K;
        X += Lowbit(X);
    }
} 

int Sum(int X) {
    int Ans = 0;
    while(X) {
        Ans += Tree[X];
        X -= Lowbit(X);
    }
    return Ans;
}

char Or[MaxN], A[MaxN];
int Q[MaxN], Cur = 0, Ret = 0;

void Insert(char *S, int Root) {
    for(int i = 0; S[i]; i++) {
        if(S[i] == 'P') Q[++Ret] = Root; 
        else {
            if(S[i] == 'B') Root = Ac[Root].Fa;
            else {
                int Now = S[i] - 'a';
                if(!Ac[Root].Vis[Now]) Ac[Root].Vis[Now] = P, Ac[P].Fa = Root, P += 1;
                Root = Ac[Root].Vis[Now];
            }
        }
    Ac[Root].End = 1;
    }
}

void Build() {
    std::queue<int> Que;
    for(int i = 0; i < 26; i++) if(Ac[0].Vis[i]) Ac[Ac[0].Vis[i]].Fail = 0, Que.push(Ac[0].Vis[i]);
    while(!Que.empty()) {
        int Top = Que.front(); Que.pop();
        for(int i = 0; i < 26; i++) {
            int Vis = Ac[Top].Vis[i];
            if(Vis) {
                Ac[Vis].Fail = Ac[Ac[Top].Fail].Vis[i];
                Que.push(Ac[Top].Vis[i]);
            }
            else Ac[Top].Vis[i] = Ac[Ac[Top].Fail].Vis[i];
        }
    }
}

int Dfn[MaxN], Time = 0, R[MaxN];

void Dfs(int Now) {
    Dfn[Now] = ++Time;
    for(int i = Last[Now]; i; i = Road[i].Next) {
        int To = Road[i].To;
        Dfs(To);
    }
    R[Now] = Time;
}

int Tot[MaxN];
int Ans[MaxN];

int main() {
    scanf("%s", Or);
    Insert(Or, 0); Build();
    std::vector <Query> Ask[MaxN];
    for(int i = 1; i < P; i++) Add(Ac[i].Fail, i);
    Dfs(0); int Root = 0; scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        int X, Y; scanf("%d%d", &X, &Y);
        Ask[Y].push_back((Query) {X, i});
    }
    Update(Dfn[0], 1);
    Ret = 0; 
    for(int i = 0; Or[i]; i++) {
        if(Or[i] == 'P') {
            Ret += 1;
            for(int j = 0; j < Ask[Ret].size(); j++) {
                int X = Q[Ask[Ret][j].X];
                Ans[Ask[Ret][j].Y] = Sum(R[X]) - Sum(Dfn[X] - 1);
            }
        }
        else if(Or[i] == 'B') Update(Dfn[Root], -1), Root = Ac[Root].Fa;
        else Root = Ac[Root].Vis[Or[i] - 'a'], Update(Dfn[Root], 1);
     }
    for(int i = 0; i < N; i++) printf("%d\n", Ans[i]);
} 