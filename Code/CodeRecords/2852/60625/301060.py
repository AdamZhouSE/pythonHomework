#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int a[100005];
int b[100005]; 
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>a[i];
		fill(b,b+n,1);//与mesert 
	int j=0;
	//a[]  2 2 2 1 1 2 2 
	//b[]  1 1 1 1 1 1 1 
	for(int i=1;i<n;i++){
		if(a[i]==a[i-1])
            b[j]++;
        else
            j++;
	}
	int sum=0;
	for(int i=1;i<=j;i++){
		sum=max(sum,min(b[i],b[i-1]));
	}
	cout<<sum*2<<endl;
	return 0;
} 