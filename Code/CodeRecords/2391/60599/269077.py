#include<iostream>
#include<cstring>
#include<cstdio>
#define M 400000        //数组要开到足够大
using namespace std;
int n, m, tot;
int f[M], trie[M][26];
char s[26];

void insert() {        //插入操作
    int len = strlen(s);
    int root = 0;
    for(int i = 0; i < len; i++) {
        int id = s[i] - 'a';
        if(!trie[root][id]) trie[root][id] = ++tot;
        root = trie[root][id];
    }
    f[root] = 1;        //每个单词起始时都赋为 1
}
void find() {        //查询操作  注意输出全为大写！！
    int len = strlen(s);
    int root = 0;
    for(int i = 0; i < len; i++) {
        int id = s[i] - 'a';
        if(trie[root][id]==0) { printf("WRONG\n"); return ; }
        root = trie[root][id];
    }
    if(f[root]==-1) printf("REPEAT\n");
    else printf("OK\n"), f[root] = -1;        //已查询过赋值为 -1
}

int main() {
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        cin >> s;
        insert();
    }
    scanf("%d", &m);
    for(int i = 1; i <= m; i++) {
        cin >> s;
        find();
    }
    return 0;
}