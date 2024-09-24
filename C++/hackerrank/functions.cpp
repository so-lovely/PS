#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
int maximum(int& a, int& b, int& c, int& d){
    set<int> s { a, b, c, d};
    return *s.rbegin();
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a; int b; int c; int d; int max;
    cin >> a >> b >> c >> d;
    max = maximum(a,b,c,d);
    cout << max << endl;
    return 0;
}
