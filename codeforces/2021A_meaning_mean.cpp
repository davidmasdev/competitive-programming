// David Mas
// https://codeforces.com/problemset/problem/2021/A
// data structures, greedy, math, sortings, 800
#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, x;
    cin >> n;
    vector<int> a(n);

    for(int i=0; i<n; i++)
        cin >> a[i];
        
    while(a.size() > 1) {
        sort(a.begin(), a.end());
        x = floor((a[0] + a[1]) / 2);
        a.erase(a.begin(), a.begin()+2);
        a.push_back(x);
    }

    cout << a[0] << "\n";
        
    
}

int main() {
    int t;
    cin >> t;
    while(t--) solve();
}