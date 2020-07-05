#include<iostream>///用例好水
using namespace std;  

unsigned long long min(unsigned long long a, unsigned long long b, unsigned long long c) {
	if (a < b)	if (a < c)return a;
				else return c;
	else 		if (b < c)return b;
				else return c;
}

unsigned long long Ugly(int number) {
	unsigned long long ugly2, ugly3, ugly5;
	int ptr = 0;
	int ptr2=0,ptr3=0,ptr5=0; 
	int temporary_ptr;
	unsigned long long ugly[15000];
	ugly[0] = 1;

	while (ptr < number-1) {
		ugly2 = ugly[ptr] / 2 + 1;														//此时2*ugly2恰大于ugly[ptr]
		ugly3 = ugly[ptr] / 3 + 1;
		ugly5 = ugly[ptr] / 5 + 1;
		for (temporary_ptr = ptr2; ugly[temporary_ptr] < ugly2; temporary_ptr++);//使ugly[temporarily_ptr] >= ugly2 
		ugly2 = 2 * ugly[temporary_ptr];											   //ugly2可能是下一个丑数 
		ptr2=temporary_ptr;
		for (temporary_ptr = ptr3; ugly[temporary_ptr] < ugly3; temporary_ptr++);//这里最好用while{;;}
		ugly3 = 3 * ugly[temporary_ptr];			
		ptr3=temporary_ptr;
		for (temporary_ptr = ptr5; ugly[temporary_ptr] < ugly5; temporary_ptr++);//不应该用for(;;); 
		ugly5 = 5 * ugly[temporary_ptr];
		ptr5=temporary_ptr;
		ptr++;
		ugly[ptr] = min(ugly2, ugly3, ugly5);											//求最小值 
	}
	//for(int i=1;i<=number;i++)cout<<i<<' '<<ugly[i-1]<<endl; 
	return ugly[ptr];
}
int main() {
	int number;
	cin  >> number;
	Ugly(number);
	cout << Ugly(number) << endl;
}