#include <bits/stdc++.h>
using namespace std;
string str;
map<string, int> smap;
int N;
long res(0);
string sn[10001];


void init()
{
    cin >> str >> N;
    for(int i=0; i<N; ++i) cin >> sn[i];
    for(int i=0,n=str.size(); i<=(n-8); ++i) {
        string ts = str.substr(i,8);
        if(smap.find(ts)==smap.end()) {
            smap[ts] = 1;
        } else {
            smap[ts] += 1;
        }
    }

}

void doit()
{
    for(int i=0; i<N; ++i) {
        char* s = new char[sn[i].size()+1];
        strcpy(s,sn[i].c_str());
        sort(s,s+strlen(s)); 
        do {
            if(smap.find(s)!=smap.end()) {  
                res += smap[s];
            }   
        }while(next_permutation(s,s+strlen(s)));

    }
} 

int main()
{
    init();
    doit(); 
    cout << res << endl;
    return 0;
}