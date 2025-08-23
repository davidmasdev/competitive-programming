// David Mas
// https://codeforces.com/problemset/problem/1791/A 
// implementation, strings, 800
#include <bits/stdc++.h>

using namespace std;

void solve() {
    char c;
    cin >> c;
    string codeforces = "codeforces";
    bool check = false;
    for(auto ch : codeforces)
        if(ch==c)
            check = true;

    if(check)
        cout << "YES\n";
    else
        cout << "NO\n";

}

int main() {
    int t;
    cin >> t;

    while(t--) solve();
}