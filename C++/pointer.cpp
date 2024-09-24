#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void sum(int* p1, int* p2, int* result){
    *result = *p1 + *p2;
}

void abs(int* p1, int* p2, int* result){
    if(*p1>=*p2){
        *result = +(*p1)-(*p2);
    }
    else{
        *result = -(*p1)+(*p2);
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a; int b;
    scanf("%d", &a);
    scanf("%d", &b);
    int* p1 = &a;
    int* p2 = &b;
    int c = 0;
    int *result = &c;
    sum(p1, p2, result);
    printf("%d\n", c);
    abs(p1, p2, result);
    printf("%d", c);
    
       
    return 0;
}
