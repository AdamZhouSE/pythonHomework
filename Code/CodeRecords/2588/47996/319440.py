#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;

bool isPrime(int n) {
    if (n <= 3) {
        return n > 1;
    }
    int k = (int)sqrt((double)n);
    int i;
    for (i = 2; i <= k; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int sumgewei(int num) {
    int sumg = 0;//各位之和
    while (num) {
        sumg += num % 10;//计算每一位的和
        num = num / 10;
    }
    return sumg;
}

int main() {
    int n, num;
    scanf("%d", &num);
    while(num-->0){
        scanf("%d", &n);
        if (isPrime(n)) {
            //素数不是smith数
            printf("0\n");
        }
        else {
            int sumg = sumgewei(n);//各位之和n
            int sump = 0;//质因子之和
            for (int i = 2; i <= n;) {
                if ((n%i == 0) && isPrime(i)) {
                    sump += sumgewei(i);
                    n = n / i;
                }
                else {
                    i++;
                }
            }
            if (sumg == sump) {
                printf("1\n");
            }
            else {
                printf("0\n");
            }
        }
    }
    return 0;
}