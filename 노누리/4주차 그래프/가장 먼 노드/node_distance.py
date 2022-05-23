# 계속 같은 구간만 반복했던 풀이
# visited와 graph를 잘 생각해보고 코드를 짜야할 것 같다

# from collections import deque
# def solution(n, edge):
#     answer = 0
#     graph=[[0]*n for _ in range(n)]
#     queue=deque([])
    
#     for i in edge:
#         x,y=i
#         graph[x-1][y-1]=1
#         graph[y-1][x-1]=1
#         if x==1:
#             queue.append((0,y-1))
#         elif y==1:
#             queue.append((0,x-1))
    
#     while queue:
#         a,b=queue.popleft()
#         for j in range(n):
#             if graph[b][j]==1 and a!=j:
#                 graph[b][j]=graph[a][b]+1
#                 queue.append((b,j))
#     return answer



from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n + 1)]
    visited=[-1]*(n+1)
    queue=deque([(1,0)])

    for i in edge:
        x,y=i
        graph[x].append(y)
        graph[y].append(x)

    while queue:
        a,dis=queue.popleft()
        if visited[a]==-1:
            visited[a]=dis
            for gr in graph[a]:
                queue.append((gr,dis+1))

    for i in range(len(visited)):
        if visited[i]==max(visited):
            answer+=1

    return answer
