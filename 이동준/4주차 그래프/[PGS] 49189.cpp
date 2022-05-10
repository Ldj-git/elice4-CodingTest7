#include <string>
#include <vector>
#include <queue>

using namespace std;

// [PGS] 49189. 가장 먼 노드 / 레벨 3 / 25분

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;

    vector<int>tmp(n,0);
    vector<vector<int>>ad(n, tmp);
    //그래프화
    for (int i = 0; i < edge.size(); i++) {
        int s = edge[i][0] - 1, e = edge[i][1] - 1;
        ad[s][e] = 1; ad[e][s] = 1;
    }

    //그냥 bfs한번 돌리고 결과 보면서 가장 먼 노드 거리 찾아서 카운트
    vector<int>dist(n, -1); //visited 겸용
    queue<int>q; q.push(0);
    dist[0] = 0;
    while (!q.empty()) {
        int here = q.front(); q.pop();
        for (int i = 0; i < n; i++) {
            if (ad[here][i] == 1) {//갈수 있고
                if (dist[i] == -1) {//방문 안했으면
                    dist[i] = dist[here] + 1;
                    q.push(i);
                }
            }
        }
    }

    int max = -1;
    for (int i = 0; i < n; i++) {
        if (max < dist[i])
            max = dist[i];
    }
    for (int i = 0; i < n; i++) {
        if (max == dist[i])
            answer++;
    }


    return answer;
}