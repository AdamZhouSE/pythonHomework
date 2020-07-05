#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

struct node{
    int x,y;
};

bool cmp(node a,node b){
    if( a.x != b.x ){
        return a.x < b.x;
    }
    return a.y < b.y;
}

int main() 
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        long long int Total=0,sum=0;
        node arr[n];
        map<int,int> m1,m2;
        for(int i=0; i<n; i++){
            cin>>arr[i].x>>arr[i].y;
        }
        sort(arr,arr+n,cmp);
        m1[arr[0].x]++;     m2[arr[0].y]++;
        for(int i=1; i<n; i++){
            if( arr[i].x==arr[i-1].x && arr[i].y==arr[i-1].y ){
                continue;
            }
            m1[arr[i].x]++;  
            m2[arr[i].y]++;
        }
        map<int,int>::iterator i;
        for(i=m1.begin(); i!=m1.end(); i++){
            Total = i->second;
            Total*=(Total-1);
            Total/=2;
            sum+=Total;
        }
        for(i=m2.begin(); i!=m2.end(); i++){
            Total = i->second;
            Total*=(Total-1);
            Total/=2;
            sum+=Total;
        }
        cout<<sum<<endl;
    }
    
	return 0;
}