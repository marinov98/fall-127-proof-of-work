#include <iostream>
using namespace std;
int caught_speeding(int speed, bool is_birthday) {
  int ans = 0;
  if (!is_birthday) {
    if (speed >= 61) {
      ans++;
    }
    if (speed > 80) {
      ans++;
    }
  }
    else {
      if (speed >= 66) {
        ans++;
      }
      if (speed > 86) {
        ans++;
      }
    }
  return ans;
}
bool cigar_party(int cigars, bool is_weekend) {
    bool ans = true;
    if ((!is_weekend and cigars > 60) or cigars <= 40) {
      ans = false;
    }
    return ans;
}
int lone_sum(int a,int b, int c){
  int sum=0;
  if (a!=b and a!=c);{
    sum+=a
  }
  if (c!=b and c!=a);{
    sum+=c
  }
  if (b!=a and b!=b){
  sum+=b
  }
  return 0;
}

int main() {
  cout << caught_speeding(61, true);
  cout << cigar_party(50, false);
  cout << lone_sum(3, 2, 3);
}
