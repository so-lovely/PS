#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>


using namespace std;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a;
    int b;
    array<string, 9> number {"one", "two", "three", "four",
                            "five", "six", "seven", "eight", "nine"};
    cin >> a >> b;
    if(!(a<=b)){
        exit(0);
    }
    for (int n=a ; b-n>=0 ; n++){
        if(1<=n && n <= 9){
            cout << number[n-1] << endl;
        }
        else if(n>9 && (n % 2 ==0)){
            cout << "even" << endl;
        }
        
        else if(n>9 && (n % 2==1)){
            cout << "odd" << endl;
        }
        
    }
    return 0;
}
