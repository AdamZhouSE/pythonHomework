#include <iostream>
#include <map>
#include <string>
#define N 100001
using namespace std;
map<string,int>num;
int n,a[N],pos[N],size,sum[N],dot[N];
long long ans=0;
inline void insert(int num)
{
    for(int i=1;i<pos[num];i++)ans+=sum[i];
    for(int i=(pos[num]-1)*size+1;i<num;i++)ans+=dot[i];
    dot[num]++;
    sum[pos[num]]++;
    return;
}
int main()
{
    cin>>n;
    string s;
    for(int i=1;i<=n;i++)
    {
        cin>>s;
        num[s]=i;//离散化
    }
    for(int i=1;i<=n;i++)
    {
        cin>>s;
        a[i]=num[s];
    }
    for(size=1;size*size<=n;size++);size--;
    for(int i=1;i<=n;i++)pos[i]=(i-1)/size+1;
    for(int i=n;i>=1;i--)
    {
        insert(a[i]);
    }
    cout<<ans<<endl;
    return 0;
}