#include <iostream>
using namespace std;

// 울타리 / 하 / 20분

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    //시계방향으로
    int x1, y1, x3, y3;
    int x, y; cin >> x >> y;

    x1 = x - 1; y1 = y - 1;
    x3 = x + 1; y3 = y + 1;

    for (int i = 1; i < k; i++) {
        cin >> x >> y;
        if (x1 >= x) {
            x1 = x - 1;
        }
        if (y1 >= y) {
            y1 = y - 1;
        }
        if (x3 <= x) {
            x3 = x + 1;
        }
        if (y3 <= y) {
            y3 = y + 1;
        }
    }

    cout << (x3 - x1) * 2 + (y3 - y1) * 2;
}