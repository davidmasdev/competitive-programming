// David Mas
// https://codeforces.com/problemset/problem/2130/A
// greedy, math, 800
#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, s, score = 0;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> s;
        score += s + (s==0);
    }
    cout << score << "\n";
}

int main() {
    int t; 
    cin >> t;
    while(t--) solve();
}