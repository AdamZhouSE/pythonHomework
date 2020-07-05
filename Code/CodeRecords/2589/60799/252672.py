#include<bits/stdc++.h>
#define mol 1000000007
void function2(long long int a[2][2], long long int b[2][2]) {
	int i, j;
	long long int c[2][2];
	for (i = 0; i <= 1; i++)for (j = 0; j <= 1; j++) {
		c[i][j] = ((a[i][0] * b[0][j]) % mol + (a[i][1] * b[1][j]) % mol) % mol; 
	}
	for (i = 0; i <= 1; i++)for (j = 0; j <= 1; j++) {
		a[i][j] = c[i][j];
	}
}
void function(long long int a[2][2], long long int n) {//次方 

	int i, j;
	if (n == 1)return;
	if ((n & 1) == 0)
	{
		function(a, n / 2); function2(a, a);
	}
	else {
		long long int c[2][2];
		for (i = 0; i <= 1; i++)for (j = 0; j <= 1; j++)c[i][j] = a[i][j];
		function(a, n / 2); function2(a, a); function2(a, c);
	}
}
int main() {
	int TEST;
	std::cin >> TEST;
	for (int test = 0;test<TEST;test++){
		long long int n;
		std::cin >> n;
		long long int helper[2][2];
		helper[0][0] = 1;
		helper[0][1] = 1;
		helper[1][0] = 1;
		helper[1][1] = 0;

		long long int base[2][2];
		base[0][0] = 2;
		base[0][1] = 1;
		base[1][0] = 1;
		base[1][1] = 0;

		if (n == 0)printf("2");
		else if (n == 1)printf("1");
		else if (n == 2)printf("3");
		else {
			function(helper, n - 2);
			function2( helper, base);
			printf("%lld", (helper[0][0]+helper[0][1]) % mol);
		}
		printf("\n");
	}
	getchar(); getchar();
	return 0;
}