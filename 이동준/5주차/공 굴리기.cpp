#include <iostream>
#include <vector>
using namespace std;

// 공 굴리기 / 중 / 50분

int main() {
    int n, m, ret = -1; cin >> n >> m;
    vector<vector<int>>map;
    for (int i = 0; i < n; i++) {
        vector<int> ttmp;
        for (int j = 0; j < m; j++) {
            int tmp; cin >> tmp;
            ttmp.push_back(tmp);
        }
        map.push_back(ttmp);
    }
    int x, y; cin >> y >> x;
    x--; y--;

    vector<bool>v(m, false);
    vector<vector<bool>>visited(n, v);

    //상좌우하
    int dirx[5] = { 999,0,-1,1,0 };
    int diry[5] = { 999,-1,0,0,1 };

    //지도 벗어나면 종료
    while (x >= 0 && x < m && y >= 0 && y < n) {
        if (visited[y][x]) {
            //반복되는 구간 길이 측정
            visited.assign(n, v);
            ret = 0;
            while (!visited[y][x]) {
                visited[y][x] = true;
                int dir = map[y][x];
                y += diry[dir];
                x += dirx[dir];
                ret++;
            }
            cout << ret;
            return 0;
        }
        visited[y][x] = true;
        int dir = map[y][x];
        y += diry[dir];
        x += dirx[dir];
        
    }
    cout << ret;
}