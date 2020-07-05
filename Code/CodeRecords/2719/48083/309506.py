#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
using namespace std;
struct Plan{
    int l,r;
    bool operator <(const Plan &rhs)const{
        return r<rhs.l;
    }
};
int T;
set<Plan> s;
int main(){
    cin>>T;
    while(T--){
        char c; scanf(" %c",&c);
        if(c=='A'){
            int l,r,cnt=0; scanf("%d %d",&l,&r);
            Plan tmp=(Plan){l,r};
            set<Plan>::iterator it=s.find(tmp);
            while(it!=s.end()){
                ++cnt; s.erase(it);
                it=s.find(tmp);
            }
            s.insert(tmp);
            printf("%d\n",cnt);
        }
        else{
            printf("%d\n",s.size());
        }
    }
    return 0;
}