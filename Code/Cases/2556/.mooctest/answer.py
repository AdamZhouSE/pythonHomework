#include<bits/stdc++.h>
using namespace std;
const int N=50005;
typedef pair<int,int> pii;
pii p[N];
int main()
{
    int n,k;
    cin>>n>>k;
    for(int i=1;i<=n;i++)
        cin>>p[i].first>>p[i].second;
  //first表示横坐标 second表示纵坐标
    sort(p+1,p+n+1);
  //横坐标为第一关键字 纵坐标为第二关键字排序
    set<pii> S;
  //first表示纵坐标 second表示点的标号 其实只保存点的标号也可以 但必须自定义比较函数了
    long long ans=0;
    for(int i=1,j=1;i<=n;i++)
    {
        for(;j<i&&p[i].first-p[j].first>=k;j++)
            S.erase(make_pair(p[j].second,j));
      //删除不满足条件的点
        set<pii>::iterator it1=S.insert(make_pair(p[i].second,i)).first,it2=it1;
      //it1和it2均为当前点的迭代器
        if(it1--!=S.begin()&&p[i].second-it1->first<k)
            if(!ans)
                ans=(long long)(k-abs(p[i].first-p[it1->second].first))*(k-(p[i].second-it1->first));
            else
                ans=-1;
        if(++it2!=S.end()&&it2->first-p[i].second<k)
            if(!ans)
                ans=(long long)(k-abs(p[i].first-p[it2->second].first))*(k-(it2->first-p[i].second));
            else
                ans=-1;
      //注意set::iterator只能进行自增自减 不能进行+1/-1
    }
    cout<<ans<<endl;
    return 0;
}