#include <string>
#include <vector>

using namespace std;

//[PGS] 49191. 순위 / 레벨 3 / 2시간 이상

//생각 안나서 힌트봄

// DFS로 탐색한다 => 처음 시작하는 부모 노드가 나머지 자식 노드를 다 이길수 있다는 뜻입니다!
// 순위를 알 수 있다 => 모든 노드와의 관계를 알고 있다는 뜻 입니다!
// 이 두가지만 알면 해결 할 수 있습니다.

vector<bool>visited;

void dfs(vector<vector<int>> r, int here) {
    for (int i = 0; i < r.size(); i++) {
        if (r[i][0] == here && !visited[r[i][1]]) {
            visited[r[i][1]] = true;
            dfs(r, r[i][1]);
        }
    }
}

int count(vector<bool>v) {
    int ret = 0;
    for (int i = 1; i < v.size(); i++) {
        if (v[i])
            ret++;
    }
    return ret;
}

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    //모든 노드에 대해 정방향, 역방향 dfs 돌리기
    //그래서 도달한 모든 노드가 n-1개면 순위 알 수 있는 놈

    //역방향 엣지 만들기
    vector<vector<int>>reverse;
    for (int i = 0; i < results.size(); i++) {
        reverse.push_back({ results[i][1],results[i][0] });
    }

    for (int i = 1; i <= n; i++) {
        int tmp = 0;
        //정방향
        visited.assign(n + 1, false);
        dfs(results, i);
        tmp += count(visited);

        //역방향
        visited.assign(n + 1, false);
        dfs(reverse, i);
        tmp += count(visited);

        if (tmp == n - 1)
            answer++;
    }

    return answer;
}