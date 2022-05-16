from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[]* n for _ in range(n+1)] 

    # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0]*(n+1)
    visited[1] = 1  # 1번 노드에서 가장 먼 노드 찾기
    # print(graph)
    queue = deque([1])

    # BFS
    while(queue):   # 빈 배열이면 false
        n = queue.popleft()
        for i in graph[n]:  # 3, 2
            # print(i)
            if visited[i] == 0: # 한 번도 방문하지 않은 노드
                queue.append(i)
                visited[i] = visited[n]+1   # 깊이
                # print("visited[{0}]: {1}".format(i, visited[i]))

    answer = visited.count(max(visited)) # 가장 깊은 노드의 개수
    return answer


# def solution(n, edge):
#     answer = 0
#     graph = {i: [] for i in range(1, n+1)}
    
#     # {1: {2, 3}, 2: {1, 3, 4, 5}, 3: {1, 2, 4, 6}, 4: {2, 3}, 5: {2}, 6: {3}}
#     for e in edge:
#         graph[e[0]].append(e[1])
#         graph[e[1]].append(e[0])
            
#     root = 1
#     visited = [0] * (n+1)
#     visited[1] = 1 # 1번 노드에서 가장 멀리 떨어진 노드의 갯수
#     queue = deque([root])
        
#     while queue:    # 배열이 비면 false
#         n = queue.popleft()

#         for i in graph[n]:
#             queue.append(i)
#             visited[i] += 1
#             print(i, queue)

#     answer = max(visited)
    
#     return answer

if __name__ == "__main__":
    
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))