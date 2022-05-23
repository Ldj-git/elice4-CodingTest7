# 40분정도 고민하다가 블로그 참고... 그새 dfs 구현방법을 잊어버렸다... 이놈의 기억력....

from collections import deque


def solution(n, edge):
    answer = 0

    # 1로 부터 각 정점의 거리
    distance = [-1 for _ in range(n+1)]
    # 그래프
    graph = [[] for i in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # dfs
    q = deque([1])
    distance[1] = 0  # 시작과 동시에 방문
    while q:
        now = q.popleft()
        if graph[now]:
            for i in graph[now]: 
                if distance[i] == -1:  # 방문 안 했을 경우
                    q.append(i)
                    distance[i] = distance[now] + 1 

    max_distance = max(distance)
    for i in range(len(distance)):
        if max_distance == distance[i]:
            answer += 1

    return answer
