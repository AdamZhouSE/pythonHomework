#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int x;
	double m, sum = 0;
	int p[1000];
	cin >> x;
	for (int i = 0; i < x; i++)
	{
		cin >> p[i];
		sum = sum + p[i];
	}
	m = sum / x;
	cout << fixed << setprecision(6) << m << endl;
}