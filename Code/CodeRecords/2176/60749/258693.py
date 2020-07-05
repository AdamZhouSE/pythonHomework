
#include <bits/stdc++.h>
#define For(a, b, c) for (int a = b; a <= c; ++a)
using namespace std;
const int N = 1000007;
char S[N];
int n, A[N];
bool cmp(int i, int j) { return strcmp(S + i, S + j) < 0; }
main() {
    scanf("%s", S + 1), n = strlen(S + 1);
    For(i, 1, n) A[i] = i;
    sort(A + 1, A + 1 + n, cmp);
    For(i, 1, n) printf("%d ", A[i]);
    return 0;
}