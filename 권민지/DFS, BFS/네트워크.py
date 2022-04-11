def dfs(node, visited, computers):
    visited[node] = 1  # 방문 처리

    for i in range(len(computers)):
        if node != i and computers[node][i] == 1 and visited[i] == 0:
            dfs(i, visited, computers)


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, computers)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
