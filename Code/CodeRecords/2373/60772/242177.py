#include <stdio.h>
int main(void){
    while(scanf(“%s”,a)!=EOF) { 
    l=strlen(a); 
    for (i=0;i=l/2;i++) { 
        if(a[i]!=a[l-I-1]) {
            printf(“NO”);
            break;
        } 
    } 
    if (i>=l/2) printf(“YES”); 
    }
}