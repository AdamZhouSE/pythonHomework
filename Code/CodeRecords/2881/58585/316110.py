#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cctype>
#include <cmath>
#include <algorithm>
#define THE_BEST_PONY "Rainbow Dash"

using namespace std;
int n;

void PrintAns(int x){
    for(int i=0;i<(n-x)/2;i++) printf("*");
    for(int i=0;i<x;i++) printf("D");
    for(int i=0;i<(n-x)/2;i++) printf("*");
    printf("\n");
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=(n-1)/2+1;i++) PrintAns(i*2-1);
    for(int i=(n-1)/2;i>0;i--) PrintAns(i*2-1);
    return 0;
}