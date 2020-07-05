#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int a[10010];
int cmp(const void *x, const void *y){
return *(int *)x - *(int *)y;
}
int main(){
int n, m, k, mov = 0;
int i, j, flag = 1;
scanf("%d%d%d", &n, &m, &k);
for(i = 0; i < n*m; i++)
scanf("%d", a+i);
for(i = 1; i < n*m; i++){
if((a[i] - a[i-1]) % k){
flag = 0;break;
}
}
if(!flag) printf("-1\n");
else{
qsort(a, n*m, sizeof(int), cmp);
j = n*m/2;
for(i = 0;i < n*m; i++)
mov += abs((a[i] - a[j])/k);
printf("%d\n", mov);
}
return 0;
}