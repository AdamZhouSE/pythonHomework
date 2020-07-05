#include <iostream>
using namespace std;
int main()
{
	int n,m,pos=0,minus=0,t;
	cin >> n >> m;
	for(int i=0;i<n;i++) {
		cin >> t;
		if(t == 1)
			pos++;
		else
			minus++;
	}
	int l,r,interv;
	for(int i=0;i<m;i++) {
		cin >> l >> r;
		interv = r-l+1;
		if(interv & 1) {
			cout << "0\n";
			continue; 
		}
		interv /= 2;
		if(interv > pos || interv > minus) {
			cout << "0\n";
			continue;
		}
		cout << "1\n";
	}
}