// David Mas
// https://codeforces.com/problemset/problem/1154/A
// math, 800
#include <bits/stdc++.h>

using namespace std;

int main() {
  vector<int> x(4);
  int maxnum = 0;

  for(int i=0; i<4; i++) {
    cin >> x[i];
    maxnum = max(maxnum, x[i]);
  } 

  x.erase(find(x.begin(), x.end(), maxnum));

  int a = maxnum - x[0], b = maxnum - x[1], c = maxnum - x[2];
  cout << a << " " << b << " " << c << "\n";
}
