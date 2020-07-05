#include<iostream>
#include<string>
#include<istream>

using namespace std;

void main() {
	char ch;
	string s;
	string tmp;
	int y; //year
	int m; //month
	int d; //day
	int res; //result
	int isleap = 0; //leap year
	int sum = 0;

	cin >> s;
	tmp = s.substr(0, 4);
	y = stoi(tmp);
	tmp = s.substr(5, 2);
	m = stoi(tmp);
	tmp = s.substr(8, 2);
	d = stoi(tmp);

	if (y % 4 == 0 & y % 100 != 0) {
		isleap = 1;
	}
	else if (y % 400 == 0) {
		isleap = 1;
	}
	else {
		isleap = 0;
	}

	int dict[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	sum = d;
	for (size_t i = 1; i <= m-1; i++) {
		sum = sum + dict[i];
	}

	if (m >= 3 & isleap) {
		sum++;
	}

	if ((m != 2 & d > dict[m]) | (m == 2 & isleap != 1 & d > dict[m]) | (m == 2 & isleap == 1 & d > dict[m] + 1)) {
		cout << "-1";
		
	}
	else {
		cout << sum;
	}


	//system("pause");
}