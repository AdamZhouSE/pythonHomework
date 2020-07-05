#include<bits/stdc++.h>
#define FOR(i,l,r) for(register int i=l;i<=r;i++)
using namespace std;

typedef long long ll;

const int maxn=5e5+2000;

multiset<int>mt;
char str[3];int l,r;
pair<int,int>color[maxn];
int col[maxn];
bool vis[maxn];
vector<int>G;

int main(){
    int T;cin>>T;
    while(T--){
        scanf("%s",str);
        if(str[0]=='A'){
            scanf("%d%d",&l,&r);
            auto itl=mt.lower_bound(l);
            auto itr=mt.upper_bound(r);
            for(auto it=itl;it!=itr;it++){
                int c=col[(*it)];
                if(vis[c])continue;vis[c]=true;
                int L=color[c].first,R=color[c].second;
                G.push_back(L);G.push_back(R);
            }
            if(G.size()==0){
                if(itl==mt.begin()||itr==mt.end());
                else{
                    --itl;
                    if(col[(*itl)]==col[(*itr)]){
                        int c=col[(*itl)];
                        vis[c]=true;
                        int L=color[c].first,R=color[c].second;
                        G.push_back(L);G.push_back(R);
                    }
                }

            }
            for(auto it:G)mt.erase(it);
            printf("%d\n",G.size()/2);
            G.clear();
            mt.insert(l);mt.insert(r);
            color[T]=make_pair(l,r);
            col[l]=col[r]=T;
        }
        if(str[0]=='B'){
            printf("%d\n",mt.size()/2);
        }
    }
}