#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 사무실 짓기 / 중 / 틀림..

int main() {
    //이진탐색도 생각나긴 하는데 그냥 완탐으로 해봄 일단
    int n; cin >> n;
    vector<int> zib;
    int minn = 1000000, maxx = 0;
    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp;
        minn = min(minn, tmp);
        maxx = max(maxx, tmp);
        zib.push_back(tmp);
    }

    int ret = 1;
    long long dist = LLONG_MAX;
    for (int i = minn; i <= maxx; i++) {
        long long tmp = 0;
        for (int j = 0; j < n; j++) {
            tmp += zib[j] - i >= 0 ? zib[j] - i : i - zib[j];
        }
        if (dist == tmp) {
            ret++;
        }
        else {
            dist = min(dist, tmp);
        }
    }
    cout << ret;
}