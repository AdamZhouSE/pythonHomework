#include<iostream>

using namespace std;

void main() {
	int nums[10000];
	int n = 0;
	int p = 0;

	int e = 0;
	while (cin >> e) {
		nums[p] = e;
		n++;
		p++;
		if (e = getchar() == '\n') {
			break;
		}
	}
	int res = 0;
	for (int i = 0; i < n; i++) {
		int h = nums[i];
		int wid = 1;
		if (i != 0) {
			int lp = i-1;
			while (lp>=0 && nums[lp]>=h) {
				wid++;
				lp--;
			}
		}
		if (i != n - 1) {
			int rp = i + 1;
			while (rp<n && nums[rp]>=h) {
				wid++;
				rp++;
			}
		}
		if (wid*h > res) {
			res =wid*h;
		}
	}
	cout << res;

	//system("pause");
}