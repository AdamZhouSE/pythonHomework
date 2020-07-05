#include <stdio.h>
#include <string.h>
int main() {
    int n;
    while (scanf("%d",&n) != EOF) {
        int a,count1 = 0, count2 = 0;
        while (n--){
            scanf("%d",&a);
            if (a ==1) count1++;
            else if(a == 2)count2++;
        }
        int countn =count1 < count2 ? count1 : count2;
        if (count1 >count2)
            countn +=(count1 - count2) / 3;
        printf("%d\n",countn);
    }
}