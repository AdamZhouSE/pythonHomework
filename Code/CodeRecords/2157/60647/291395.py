#include <iostream>
#include<string>
using namespace std;

int match(char i) {
	if (i == 'I') {
		return 1;
	}
	else if (i == 'V') {
		return 5;
	}
	else if (i == 'X') {
		return 10;
	}
	else if (i == 'L') {
		return 50;
	}
	else if (i == 'C') {
		return 100;
	}
	else if (i == 'D') {
		return 500;
	}
	else {
		return 1000;
	}
}

int main() {
	string str,str1,str2;
	int res = 0;
	getline(cin, str);
	for (int i = 0; i < str.size(); i++) {
		if (str[i] != ' ') {
			str2 = str[i];
			str1.append(str2);
		}
		else {
			int num = 0;
			if (str1.size() > 1) {
				for (int j = 0; j < str1.size() - 1; j++) {
					if (match(str1[j]) >= match(str1[j + 1])) {
						num = num + match(str1[j]);
					}
					else {
						num = num - match(str1[j]);
					}
				}
			}
			num = num + match(str1[str1.size() - 1]);
			if (num >= res) {
				res = num;
			}
			str1.clear();
		}
		if(i==(str.size()-1) ){
			int num = 0;
			if (str1.size() > 1) {
				for (int j = 0; j < (str1.size() - 1); j++) {
					if (match(str1[j]) >= match(str1[j + 1])) {
						num = num + match(str1[j]);
					}
					else {
						num = num - match(str1[j]);
					}
				}
			}
			num = num + match(str1[str1.size() - 1]);
			if (num >= res) {
				res = num;
			}
			str1.clear(); 
		}
	}
	cout << res<<endl;
}