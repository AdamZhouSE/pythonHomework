//P1321
#include<iostream>
#include<algorithm>
#include<iomanip>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<map>
#include<queue>
using namespace std;
int boy,girl,n;
string a;
int main()
{
    cin>>a;
    n=a.length();
    for(int i=0;i<n-2;i++)
      boy+=(a[i]=='b'||a[i+1]=='o'||a[i+2]=='y');
    for(int i=0;i<n-3;i++)
      girl+=(a[i]=='g'||a[i+1]=='i'||a[i+2]=='r'||a[i+3]=='l');
    cout<<boy<<endl<<girl;               
    return 0;
}