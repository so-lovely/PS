#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    // n is first index
    // q is last query
    // k is temp index length
    int n; int q; int k; int ele;
    cin >> n >> q;
    vector<vector<int>> vec(n);
    for(int i=0; i<n; i++){
        cin >> k;
        for(int j=0; j<k; j++){
            cin >> ele;
            vec[i].push_back(ele);
        }
    }
    // vector completed
    for(int i=0; i<q; i++){
        cin >> k;
        cin >> ele;
        cout << vec[k][ele] << endl;
    }
        
    return 0;
}
