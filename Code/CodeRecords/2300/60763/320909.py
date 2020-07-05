#include<iostream>
using namespace std;

void postTra(char* pre,char* ord,int ordEnd){
    int i;
    if(*pre){
        i = 0;
        while(ord[i] && ord[i++] != *pre);
        --i;
        if(i){
            postTra(pre + 1,ord,i - 1);
        }
        if(i < ordEnd){
            postTra(pre + i + 1,ord + i + 1,ordEnd - i - 1);
        }
        cout << *pre;
    }
}

int main(void) {
    char pre[27], ord[27];
    int i;
    while (cin >> pre) {
        cin >> ord;
        i = 0;
        while (pre[i++]);
        postTra(pre, ord, i - 1);
        cout << endl;
    }
    return 0;
}